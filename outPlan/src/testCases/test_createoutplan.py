# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/12/10 15:36
# 文件: test_createoutplan.py
import sys
sys.path.append('..')
import unittest
from common.get_value import GetValue
from modules.login import Login
from modules.outplan import OutPlan
from modules.customer_manage import CustomerManage
from common.mongodb import Mongodb
import time

class TestCreateOutPlan(unittest.TestCase):
    lg = None
    data = None
    token= None
    groupId= None
    csm= None
    planId = None
    auto_test = None

    def setUp(self):
        global lg,data,token,groupId,csm

        data = GetValue()
        #登录
        lg = Login(data.getvalue('product_address'))
        res = lg.login(data.getvalue('account'), data.getvalue('product_password'))
        token=res['data']['token']
        self.assertEqual(res['data']['userName'], data.getvalue('account'))
        self.assertEqual(res['data']['accountType'], 1)

        #创建客户组手动上传号码
        csm=CustomerManage(data.getvalue('product_address'))
        res2=csm.addPhoneNumber(token,data.getvalue('userid'),['15900000000'],1,'autoTest')
        self.assertEqual(res2['status'], 1000)
        self.assertEqual(res2['msg'], '操作成功')

        #查询mongodb获取groupId
        product=Mongodb('outbound_product','phone_number','172.20.10.20',27017)
        table=product.connect_mongodb()
        res3=product.mongodb_find(table,{'userId':21,'groupName':'autoTest'})
        for item in res3:
            groupId=item['groupId']

    def test_createplan(self):
        global data,planId,auto_test
        auto_test=OutPlan(data.getvalue('product_address'))
        res=auto_test.creat_outplan(token,data.getvalue('userid'),'3706','autoTest','尚德销售纵线白名单',groupId)
        planId=res['data']['planId']
        self.assertEqual(res['status'],1000)
        self.assertEqual(res['msg'],'操作成功')

    def tearDown(self):
        #删除客户组与号码
        res=csm.deleteGroupAndCustomerPhone(token,groupId)
        self.assertEqual(res['status'], 1000)
        self.assertEqual(res['msg'], '操作成功')

        #查询mongodb外呼计划状态
        product = Mongodb('outbound_product', 'call_log', '172.20.10.20', 27017)
        table = product.connect_mongodb()

        flag=True
        while flag:
            res2 = product.mongodb_find(table, {'userId': 21, 'planName': 'autoTest', 'planId': planId})
            for item in res2:
                if item['status']==5:
                    # 删除外呼计划
                    res = auto_test.delete_outplan(token, planId)
                    self.assertEqual(res['status'], 1000)
                    self.assertEqual(res['msg'], '操作成功')
                    flag=False
            time.sleep(1)

        #注销用户
        logout=lg.logout(token)
        self.assertEqual(logout['status'],1000)
        self.assertEqual(logout['msg'],'操作成功')