# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/21 11:48
# 文件: queryscene.py
import requests
import json

class QueryScene():
    global get_queryscene_url
    get_queryscene_url='/scene/queryScene.do'

    def __init__(self,address):
        self.address=address

    def get_queryscene(self,userId):
        global  get_queryscene_url
        headers = {'Content-Type': 'application/json'}
        data={'userid':userId}
        try:
            res=requests.post(url=self.address+get_queryscene_url,headers=headers,data=json.dumps(data))
            return  json.loads(res.text)
        except Exception as e:
            print(e)