from YNT.src.common.predictor import predictor
import os

class dada:
    aList =  os.path.dirname(os.path.abspath('../..'))
    data_path = aList+'\\'+'data'+'\\'
    log_path = aList + '\\' + 'log' + '\\'

    p = predictor(data_path + "dada.txt",log_path + "dada_Log.txt","ddyy_1","10308100","20308100")
    p.func()