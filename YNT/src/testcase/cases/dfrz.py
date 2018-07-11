from YNT.src.common.predictor import predictor
import os

class dfrz:
    aList =  os.path.dirname(os.path.abspath('../..'))
    path = aList+'\\'+'data'+'\\'
    path2 = aList + '\\' + 'log' + '\\'

    p = predictor(path+"东方融资网7.1.txt",path2+"dfrz_Log.txt","dfrz_3_2","dfrz_3_2B01","10103100")
    p.func()

