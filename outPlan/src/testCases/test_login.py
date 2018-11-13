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

         lg = Login(data.getvalue('uat_address'))

     def test_login(self):
         global lg,data
         res = lg.login(data.getvalue('account'),data.getvalue('uat_password'))

         self.assertEqual(res['data']['username'],data.getvalue('account'))
         self.assertEqual(res['data']['accountType'], 1)


     def tearDown(self):
         pass






