from config.environment import AppConfig
import time

def retryBackof(callback):
    totalRetry = getattr(AppConfig, 'TOTAL_RETRY_BACKOF')
    delayTime =   getattr(AppConfig, 'DELAY_TIME_BACKOF_RETRY') 

    excute(callback,totalRetry,delayTime)

def excute(callback,totalRetry,delayTime, currentRetry=0):
    try:
        callback()
    except:
        currentRetry+=1
        if(currentRetry>totalRetry):
            raise Exception("Fail to retry")
        
        time.sleep(delayTime)
        delayTime= currentRetry*delayTime
        print(f"retry time {currentRetry}")
        excute(callback, totalRetry, delayTime, currentRetry)