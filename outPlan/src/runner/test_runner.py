# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 9:56
# 文件: test_runner.py
import HTMLTestRunner
import unittest
import datetime
from outPlan.src.common.get_path import GetPath
from outPlan.src.common.get_value import GetValue

class Runner(unittest.TestCase):
    runner=None
    path=None
    data=None

    def report(self):
        global path,data

        data=GetValue()
        now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        path=GetPath(data.getvalue('report_path')+'%s.html'%now_time)

        with open(path.get_filePath(),'wb') as fp:
            global runner
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=data.getvalue('title'),description=data.getvalue('description'))

            suiteTest = unittest.TestSuite()

            path=GetPath(data.getvalue('cases_path'))

            all_cases=unittest.defaultTestLoader.discover(path.get_filePath(),'test_*.py')

            for case in all_cases:

                suiteTest.addTest(case)

            runner.run(suiteTest)

if __name__ == '__main__':

    testrunner=Runner()
    testrunner.report()

