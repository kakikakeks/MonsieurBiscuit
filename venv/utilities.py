import time
import datetime



def getTime():
    currenttime=time.time()
    datetim=datetime.datetime.fromtimestamp(currenttime).strftime('%c')
    return datetim

