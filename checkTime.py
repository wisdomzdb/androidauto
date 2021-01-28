import datetime
import random

def TimeChuli(Time):
    newTime = Time.split(":")
    Hour = int(newTime[0])
    Minute = int(newTime[1])
    Second = int(newTime[2])
    new_time = Hour * 3600 + Minute * 60 + Second
    return new_time

def checkTime(startTime, endTime, times):
    start_time = TimeChuli(startTime)
    end_time = TimeChuli(endTime)
    nowTime = datetime.datetime.now().strftime('%X')
    now_time = TimeChuli(nowTime)
    if now_time >= start_time and now_time <= end_time:
        if end_time - now_time <= 60:
            return True
        else:
            return checkGailv(start_time, end_time, times)
    else:
        return False

def checkGailv(start_time, end_time, times):
    num = random.randint(start_time, end_time)
    if num < end_time - 10 * times:
        return False
    else:
        return True