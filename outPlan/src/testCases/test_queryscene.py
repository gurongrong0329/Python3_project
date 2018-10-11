# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 11:36
# 文件: test_queryscene.py
import sys
sys.path.append('..')
import unittest
from common.get_value import GetValue
from modules.login import Login
from modules.queryscene import QueryScene

class TestQueryScene(unittest.TestCase):
    lg = None
    data = None
    qs=None

    def setUp(self):
        global lg,data

        data = GetValue()

        lg = Login(data.getvalue('url_qa'))

        res = lg.login(data.getvalue('account'), data.getvalue('password'))

        try:
            self.assertEqual(res['data']['username'], data.getvalue('account'))
            self.assertEqual(res['data']['accountType'], 1)

        except Exception as e:
            print(e)


    def test_queryScene(self):
        global qs,data

        qs=QueryScene(data.getvalue('queryscene_url_qa'))
        res=qs.get_queryscene(data.getvalue('userid'))
        print(res)
        self.assertEqual(res['success'],True)


    def tearDown(self):
        pass