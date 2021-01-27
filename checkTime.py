import datetime

def TimeChuli(Time):
    newTime = Time.split(":")
    Hour = int(newTime[0])
    Minute = int(newTime[1])
    Second = int(newTime[2])
    new_time = Hour * 3600 + Minute * 60 + Second
    return new_time

def checkTime(startTime, endTime):
    start_time = TimeChuli(startTime)
    end_time = TimeChuli(endTime)
    nowTime = datetime.datetime.now().strftime('%X')
    now_time = TimeChuli(nowTime)
    if now_time >= start_time and now_time <= end_time:
        return True
    else:
        return False
