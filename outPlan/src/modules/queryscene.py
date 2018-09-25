# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 11:48
# 文件: queryscene.py
import requests
import json

class QueryScene():

    def __init__(self,url):
        self.url=url

    def get_queryscene(self,userId):
        headers = {'Content-Type': 'application/json'}
        data={'userid':userId}
        try:
            res=requests.post(self.url,headers=headers,data=json.dumps(data))
            return  json.loads(res.text)
        except Exception as e:
            print(e)