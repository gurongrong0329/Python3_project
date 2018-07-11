from YNT.src.common.predictor import predictor
import os


class sd:
    aList = os.path.dirname(os.path.abspath('../..'))
    path = aList + '\\' + 'data' + '\\'
    path2 = aList + '\\' + 'log' + '\\'

    p = predictor(path + "sd.txt", path2 + "sd_Log.txt", "sdjg_7", "sdjg_7B01", "10307100")
    p.func()

