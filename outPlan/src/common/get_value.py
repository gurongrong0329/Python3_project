# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/19 11:44
# 文件: get_value.py
import os

class GetValue():

     def __init__(self,datapath):
         self.datapath=datapath

     def getvalue(self,data_key):
         with open(self.datapath,'r', encoding="utf-8") as fb:
             for line in fb:

                 lines=line.strip('\n').split('=')
                 try:
                    if lines[0].strip()==data_key:
                        return lines[1].strip()
                 except Exception as e:
                        return e
         fb.close()


         