# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/17 16:17
# 文件: login.py
import requests
import json

class Login():

    def __init__(self,address):
        self.address=address
        self.login_url = '/login/doLogin.do'

    def login(self,account,password):
        headers = {'Content-Type': 'application/json'}
        data={'username':account,'password':password}

        try:
            res=requests.post(self.address+self.login_url,headers=headers,data=json.dumps(data))
            return  json.loads(res.text)
        except Exception as e:
            print(e)


