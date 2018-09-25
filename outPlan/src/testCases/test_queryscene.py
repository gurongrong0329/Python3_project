# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 11:36
# 文件: test_queryscene.py
import unittest
from outPlan.src.common.get_value import GetValue
import os
from outPlan.src.modules.login import Login
from outPlan.src.modules.queryscene import QueryScene


class TestQueryScene(unittest.TestCase):
    global lg, data,qs
    lg = None
    data = None
    qs=None

    def setUp(self):
        global lg, data

        aList = os.path.dirname(os.path.abspath('../..'))
        data_path = aList + '\\' + 'outPlan' + '\\' + 'data' + '\\parameter.txt'

        data = GetValue(data_path)

        lg = Login(data.getvalue('url'))

        res = lg.login(data.getvalue('account'), data.getvalue('password'))

        try:
            self.assertEqual(res['data']['username'], data.getvalue('account'))
            self.assertEqual(res['data']['accountType'], 1)

        except Exception as e:
            print(e)


    def test_queryScene(self):
        global qs,data

        qs=QueryScene(data.getvalue('queryscene_url'))
        res=qs.get_queryscene(data.getvalue('userid'))

        self.assertEqual(res['success'],True)


    def tearDown(self):
        pass