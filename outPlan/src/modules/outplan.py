# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/12/10 11:25
# 文件: outplan.py
from requests_toolbelt import MultipartEncoder
import requests
import json

class OutPlan():
    def __init__(self,address):
        self.address=address
        self.addCallLog_url='/outTask/addCallLog.do'
        self.deleteOutTask_url='/outTask/deleteOutTask.do'

    #form-data,创建计划
    def creat_outplan(self,token,userId,sceneId,planName,sceneName,groupId):

        data=MultipartEncoder(fields={'userId':userId,
                                      'sceneId':sceneId,
                                      'callType':'2',
                                      'planName':planName,
                                      'sceneName':sceneName,
                                      'sipIds':'8057',
                                      'createType':'2','groupIds':str(groupId)})
        headers = {'Content-Type':data.content_type, 'token': token}

        res=requests.post(url=self.address+self.addCallLog_url,headers=headers,data=data)
        return json.loads(res.text)

    #删除外呼计划
    def delete_outplan(self,token,planId):
        headers = {'Content-Type': 'application/json', 'token': token}
        data={'planId':planId}
        res = requests.post(self.address + self.deleteOutTask_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)
