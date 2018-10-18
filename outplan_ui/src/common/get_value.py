# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/9/19 11:44
# 文件: get_value.py
import sys
sys.path.append('..')
from common.get_path import GetPath

class GetValue():

     def __init__(self,datapath='data\\parameter.txt'):             #win/linux路径不同，需要修改
         path=GetPath(datapath)
         self.datapath= path.get_filePath()

     def getvalue(self,data_key):
         with open(self.datapath,'r', encoding="utf-8") as fb:
             for line in fb:
                 lines=line.strip('\n').split('=',1)
                 try:
                    if lines[0].strip()==data_key:
                        return lines[1].strip()
                 except Exception as e:
                        return e
