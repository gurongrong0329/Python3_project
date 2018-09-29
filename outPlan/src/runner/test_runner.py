# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 9:56
# 文件: test_runner.py
import HTMLTestRunner
import unittest
from outPlan.src.common.get_path import GetPath

class Runner(unittest.TestCase):
    global runner,path
    runner=None
    path=None

    def report(self):
        global path

        path=GetPath('report\\')
        with open(path.get_filePath()+ 'report.html', 'wb') as fp:
            global runner
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='外呼计划api测试报告', description='测试情况')

            suiteTest = unittest.TestSuite()

            path=GetPath('src\\testCases\\')

            all_cases=unittest.defaultTestLoader.discover(path.get_filePath(),'test_*.py')

            for case in all_cases:

                suiteTest.addTest(case)

            runner.run(suiteTest)

if __name__ == '__main__':

    testrunner=Runner()
    testrunner.report()

