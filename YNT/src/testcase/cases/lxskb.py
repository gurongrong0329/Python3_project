# 作者: admin
# 时间: 2018/7/9 9:42
# 文件: lxskb.py
from YNT.src.common.predictor import predictor
import os

class lxskb:
    aList =  os.path.dirname(os.path.abspath('../..'))
    data_path = aList+'\\'+'data'+'\\'
    log_path = aList + '\\' + 'log' + '\\'

    p = predictor(data_path + "lxskb.txt",log_path + "lxskb_Log.txt","lxsk_7","lxsk_7B01","10702100")
    p.func()