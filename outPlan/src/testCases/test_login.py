# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/18 11:25
# 文件: test_login.py
from outPlan.src.modules.login import Login
import unittest
from outPlan.src.common.get_value import GetValue

class TestLogin(unittest.TestCase):
     lg=None
     data=None

     def setUp(self):
         global lg,data,path

         data = GetValue()

         lg = Login(data.getvalue('url'))

     def test_login(self):
         global lg,data
         res = lg.login(data.getvalue('account'),data.getvalue('password'))

         try:
            self.assertEqual(res['data']['username'],data.getvalue('account'))
            self.assertEqual(res['data']['accountType'], 1)

         except Exception as e:
            print(e)

     def tearDown(self):
         pass






