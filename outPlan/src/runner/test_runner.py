# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 9:56
# 文件: test_runner.py
import HTMLTestRunner
import os
import unittest
from outPlan.src.testCases.logintest import TestLogin

class Runner(unittest.TestCase):
    global runner
    runner=None

    def report(self):
        aList = os.path.dirname(os.path.abspath('../..'))
        report_path = aList + '\\' + 'outPlan' + '\\' + 'report' + '\\'

        with open(report_path + 'report.html', 'wb') as fp:
            global runner
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
            suiteTest = unittest.TestSuite()
            suiteTest.addTest(TestLogin('test_login'))
            runner.run(suiteTest)

if __name__ == '__main__':

    testrunner=Runner()
    testrunner.report()

