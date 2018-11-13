# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/11 16:14
# 文件: customer_manage.py
import json
import requests

class CustomerManage:

    def __init__(self,address):
        self.address=address
        self.getPhoneNumList_url = '/customer/getPhoneNumList.do'
        self.getCustomerGroupById_url = '/customer/getCustomerGroupById.do'
        self.addCustomerGroup_url = '/customer/addCustomerGroup.do'
        self.deleteGroupAndCustomerPhone_url = '/customer/deleteGroupAndCustomerPhone.do'
        self.updateCustomerGroup_url = '/customer/updateCustomerGroup.do'
        self.movePhoneNumber_url = '/customer/movePhoneNumber.do'

    #获取电话号码列表
    def getPhoneNumList(self,userId):
        headers = {'Content-Type': 'application/json'}
        data={'userId':userId}
        res=requests.post(self.address+self.getPhoneNumList_url,headers=headers,data=json.dumps(data))
        return json.loads(res.text)

    #根据用户id获取客户组列表
    def getCustomerGroupById(self,userId):
        headers = {'Content-Type': 'application/json'}
        data = {'userId': userId}
        res = requests.post(self.address+self.getCustomerGroupById_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #新增客户组
    def addCustomerGroup(self,userId,groupName):
        headers = {'Content-Type': 'application/json'}
        data = {'userId': userId,'groupName':groupName}
        res = requests.post(self.address+self.addCustomerGroup_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #删除客户组的同时删除客户组下的号码
    def deleteGroupAndCustomerPhone(self,id):
        headers = {'Content-Type': 'application/json'}
        data = {'id':id}
        res = requests.post(self.address+self.deleteGroupAndCustomerPhone_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #更新客户组
    def updateCustomerGroup(self,id,groupName):
        headers = {'Content-Type': 'application/json'}
        data = {'id': id, 'groupName': groupName}
        res = requests.post(self.address+self.updateCustomerGroup_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #批量移动电话号码
    def movePhoneNumber(self,id,groupId):
        headers = {'Content-Type': 'application/json'}
        data = {'id': id, 'groupId': groupId}
        res = requests.post(self.address+self.movePhoneNumber_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)
