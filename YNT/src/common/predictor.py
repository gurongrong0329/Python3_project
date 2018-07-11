import requests
import json


class predictor(object):
    global url
    url= "http://192.168.88.16:8086/predict"

    def __init__(self,filename,logname,version,version2,id):
        self.fileName=filename
        self.logName=logname
        self.version=version
        self.version2=version2
        self.id=id


    def func(self):
        global url
        headers = {'Content-Type': 'application/json'}

        f = open(self.fileName, "r", encoding="utf-8")
        w = open(self.logName, 'w', encoding="utf-8")
        print('start------------------------------->\n')
        w.write("start------------------------------->\n")

        for line in f:
            lines = line.split()
            if len(lines) > 1:
                text = lines[1]
                cat = lines[0]

                data = {"version": self.version, "predictorId": [self.version2,self.id],
                        "content": [{"text": text, "weight": 1.0}]}
                result = requests.post(url, headers=headers, data=json.dumps(data))

                result_data = json.loads(result.text)

            if result_data['status'] == 1000:
                print('==========START==========')
                w.write('==========START==========\n')
                print("文本内容为: " + line)
                w.write("文本内容为: " + line + '\n')

                if result_data['data'] is not None and result_data['data']['result'] is not None:
                    data =  result_data['data']

                    print(json.dumps(data, ensure_ascii=False))
                    w.write(json.dumps(data, ensure_ascii=False))
                    w.write('\n')

                    if data['result'][0]['target'][0]==cat:
                        print('匹配成功')
                        w.write('匹配成功\n')

                    else:
                        print('匹配失败')
                        w.write('匹配失败\n')

                    print( '==========END============\n')
                    w.write('==========END============\n')

                else:
                    print("未匹配")
                    w.write('未匹配\n')
                    print('==========END============\n')
                    w.write('==========END============\n')

            else:
                    print("请求失败", result_data)
                    w.write("请求失败" + json.dumps(result_data, ensure_ascii=False).encode('utf-8') + "\n")
        print('end------------------------------->')
        w.write('end------------------------------->\n')
        w.close()
        f.close()
