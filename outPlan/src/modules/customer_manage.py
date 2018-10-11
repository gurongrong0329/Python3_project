# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/10/11 16:14
# 文件: customer_manage.py
import json
import requests

class CustomerManage():

    getPhoneNumList_url='/customer/getPhoneNumList.do'
    getCustomerGroupById_url='/customer/getCustomerGroupById.do'
    addCustomerGroup_url='/customer/addCustomerGroup.do'
    deleteGroupAndCustomerPhone_url='/customer/deleteGroupAndCustomerPhone.do'
    updateCustomerGroup_url='/customer/updateCustomerGroup.do'
    movePhoneNumber_url='/customer/movePhoneNumber.do'

    def __init__(self,address):
        self.address=address

    #获取电话号码列表
    def getPhoneNumList(self,userId):
        global getPhoneNumList_url
        headers = {'Content-Type': 'application/json'}
        data={'userId':userId}
        res=requests.post(self.address+getPhoneNumList_url,headers=headers,data=json.dumps(data))
        return json.loads(res.text)

    #根据用户id获取客户组列表
    def getCustomerGroupById(self,userId):
        global getCustomerGroupById_url
        headers = {'Content-Type': 'application/json'}
        data = {'userId': userId}
        res = requests.post(self.address+getCustomerGroupById_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #新增客户组
    def addCustomerGroup(self,userId,groupName):
        global addCustomerGroup_url
        headers = {'Content-Type': 'application/json'}
        data = {'userId': userId,'groupName':groupName}
        res = requests.post(self.address+addCustomerGroup_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #删除客户组的同时删除客户组下的号码
    def deleteGroupAndCustomerPhone(self,id):
        global deleteGroupAndCustomerPhone_url
        headers = {'Content-Type': 'application/json'}
        data = {'id':id}
        res = requests.post(self.address+deleteGroupAndCustomerPhone_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #更新客户组
    def updateCustomerGroup(self,id,groupName):
        global updateCustomerGroup_url
        headers = {'Content-Type': 'application/json'}
        data = {'id': id, 'groupName': groupName}
        res = requests.post(self.address+updateCustomerGroup_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)

    #批量移动电话号码
    def movePhoneNumber(self,id,groupId):
        global movePhoneNumber_url
        headers = {'Content-Type': 'application/json'}
        data = {'id': id, 'groupId': groupId}
        res = requests.post(self.address+movePhoneNumber_url, headers=headers, data=json.dumps(data))
        return json.loads(res.text)