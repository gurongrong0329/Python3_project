# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/19 11:38
# 文件: test_addgroup.py
import sys
sys.path.append('..')
from selenium import webdriver
from common.get_path import GetPath
from common.get_value import GetValue
from pages.login import Login
from pages.cusmanage import cusManage
import unittest
import time

class testAddGroupNum(unittest.TestCase):
    driver=None
    data=None
    ynt=None

    def setUp(self):
        global driver,data
        data = GetValue()
        browser = GetPath(data.getvalue('driver'))
        driver = webdriver.Chrome(browser.get_filePath())
        user = Login(driver)
        user.login(data.getvalue('address'), data.getvalue('account'), data.getvalue('password'))

    def test_addGroupNum(self):
        global driver,data,ynt
        ynt=cusManage(driver)
        ynt.cus_manage()
        time.sleep(3)
        ynt.add_group(data.getvalue('groupName'))
        time.sleep(2)

    def tearDown(self):
        global ynt,data,driver
        ynt.delete_group(data.getvalue('groupName'))
        driver.quit()
