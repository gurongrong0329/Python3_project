from YNT.src.common.predictor import predictor
import os

class ljd:
    aList =  os.path.dirname(os.path.abspath('../..'))
    path = aList+'\\'+'data'+'\\'
    path2 = aList + '\\' + 'log' + '\\'

    p = predictor(path+"xbj.txt",path2+"xbj_Log.txt","xbj_5","xbj_5","10703100")
    p.func()


