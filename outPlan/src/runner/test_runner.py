# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 9:56
# 文件: test_runner.py
import HTMLTestRunner
import os
import unittest

class Runner(unittest.TestCase):
    global runner
    runner=None

    def report(self):
        aList = os.path.dirname(os.path.abspath('../..'))
        report_path = aList + '\\' + 'outPlan' + '\\' + 'report' + '\\'
        case_path=aList + '\\' + 'outPlan' + '\\' + 'src' + '\\'+'testCases'+ '\\'

        with open(report_path + 'report.html', 'wb') as fp:
            global runner
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='外呼计划api测试报告', description='测试情况')

            suiteTest = unittest.TestSuite()
            all_cases=unittest.defaultTestLoader.discover(case_path,'test_*.py')

            for case in all_cases:

                suiteTest.addTest(case)

            runner.run(suiteTest)

if __name__ == '__main__':

    testrunner=Runner()
    testrunner.report()

