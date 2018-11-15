# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2018/11/15 14:13
# 文件: database.py
from pymongo import MongoClient

class DataBase:
    '''
    uat = DataBase('outbound_uat','phone_number')
    table = uat.connect_mongodb()
    res=uat.find(table,{'userId':21,'groupName':'测试组'})

    for item in res:
        print(item)

    '''
    def __init__(self,db_name,table_name,address='192.168.88.109',port=10001):
        self.address=address
        self.port=port
        self.db_name=db_name
        self.table_name=table_name

    def connect_mongodb(self):
        # 建立MongoDB数据库连接
        client = MongoClient(self.address,self.port)

        # 连接所需数据库,db_name为数据库名
        db = client[self.db_name]

        # 连接所用集合，也就是我们通常所说的表，table_name为表名
        table = db[self.table_name]

        return table

    def find(self,table,map):
        # 查找集合中所有数据
        return table.find(map)
