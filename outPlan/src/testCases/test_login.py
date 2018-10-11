# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/18 11:25
# 文件: test_login.py
import sys
sys.path.append('..')
from modules.login import Login
import unittest
from common.get_value import GetValue

class TestLogin(unittest.TestCase):
     lg=None
     data=None

     def setUp(self):
         global lg,data,path

         data = GetValue()

         lg = Login(data.getvalue('dev_address'))

     def test_login(self):
         global lg,data
         res = lg.login(data.getvalue('account'),data.getvalue('dev_password'))

         try:
            self.assertEqual(res['data']['username'],data.getvalue('account'))
            self.assertEqual(res['data']['accountType'], 1)

         except Exception as e:
            print(e)

     def tearDown(self):
         pass






