# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/7/19 20:04
# 文件: predictor_execel.py
import requests
import json
import xlrd

class predictor(object):
    global url
    url= "http://192.168.88.16:8086/predict"

    def __init__(self,filename,logname,version,version2,id):
        self.fileName=filename
        self.logName=logname
        self.version=version
        self.version2=version2
        self.id=id

    def readExcel(self,sheetName):
        headers = {'Content-Type': 'application/json'}
        global url

        w = open(self.logName, 'w', encoding="utf-8")
        print('start------------------------------->\n')
        w.write("start------------------------------->\n")

        #打开文件
        book=xlrd.open_workbook(self.fileName)

        #获取所有sheet
        sheets=book.sheet_names()

        #遍历sheet
        for i in sheets:
            if i ==sheetName:
                # 根据名称获取sheet内容
                sheet_cjk=book.sheet_by_name(i)
                #列数
                nclos=sheet_cjk.ncols
                #行数
                nrows=sheet_cjk.nrows
                for j in range(nclos):
                    #获取每列首行
                    true_code = sheet_cjk.cell_value(0, j)
                    #获取每列的所有值
                    textlist=sheet_cjk.col_values(j)

                    textlist2=[]
                    for k in textlist:
                        if k!='':
                            textlist2.append(k)

                    for n in range(2,len(textlist2)):

                        data = {"version": self.version, "predictorId": [self.version2,self.id],
                                "content": [{"text": textlist2[n], "weight": 1.0}]}
                        result = requests.post(url, headers=headers, data=json.dumps(data))
                        result_data = json.loads(result.text)

                        if result_data['status'] == 1000:
                            print('==========START==========')
                            w.write('==========START==========\n')
                            print("文本内容为: " + textlist2[n])
                            w.write("文本内容为: " + textlist2[n] + '\n')

                            if result_data['data'] is not None and result_data['data']['result'] is not None:
                                data = result_data['data']

                                print(json.dumps(data, ensure_ascii=False))
                                w.write(json.dumps(data, ensure_ascii=False))
                                w.write('\n')

                                if data['result'][0]['target'][0] == str(int(true_code)):
                                    print('匹配成功')
                                    w.write('匹配成功\n')
                                else:
                                    print('匹配失败')
                                    w.write('匹配失败！！！\n' + '错误的节点: ')
                                    w.write(data['result'][0]['target'][0] + '\n')
                                    w.write("正确的节点: " + str(int(true_code)) + '\n')
                                print('==========END============\n')
                                w.write('==========END============\n\n')
                            else:
                                print("未匹配")
                                w.write('未匹配\n')
                                w.write("正确的节点: " + str(int(true_code)) + '\n')
                                print('==========END============\n')
                                w.write('==========END============\n\n')
                        else:
                            print("接口请求失败", result_data)
                            w.write("接口请求失败" + json.dumps(result_data, ensure_ascii=False).encode('utf-8') + "\n")
        print('end------------------------------->')
        w.write('end------------------------------->\n')
        w.close()


    def func(self):
         self.readExcel('场景库问法')
         self.readExcel('知识库问法')






