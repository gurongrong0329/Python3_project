from YNT.src.common.predictor import predictor
import os

class ljd:
    aList =  os.path.dirname(os.path.abspath('../..'))
    path = aList+'\\'+'data'+'\\'
    path2 = aList + '\\' + 'log' + '\\'

    p = predictor(path+"ljd.txt",path2+"ljd_Log.txt","ljd_7_1","ljd_7_1B01","10703100")
    p.func()
