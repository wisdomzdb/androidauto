
import time

events = [{
        'event': 'faPengyouquan',
        'startTime': '00:00:00',
        'endTime': '00:10:00',
        'args': './发朋友圈圈素材/素材8号.txt',
    },]

#执行事件，将事件发生
def run(event):
    print('执行事件', event)
    event['done'] = "done"

#event应该在配置文件的start和end之间发生
#判断当前时间是否在start和end之间，如果在，则有概率性发生该事件，如果发生，则返回true。
#另外需要在end之前至少发生一次，所以概率应该逐渐增大，到最后一分钟时，如果还没发生过，发生的概率应该为1，即必定返回true。
#如果发生过，应该记录下来这个事件已经发生过了，不应该再次发生。
def shouldStart(event):
    #根据当前时间，start和end计算概率，如果发生，happen = 概率
    # if happen and event.happend == False:
    #     event.happend = True
    print(event.get('done'))
    if event.get('done') != 'done':
        return True
    return False

#main中每秒钟判断一次是否有事件该执行，如果有，则去执行事件
def main(events):
    while (True):
        time.sleep(1)
        for event in events:
            if shouldStart(event):
                run(event)

#TODO 这些events应该从jsonfile里读取
def parseJson():
    return [{
        'event': 'dianzan',
        'startTime': '08:00:00',
        'endTime': '10:00:00',
        'args': 'https://mp.weixin.qq.com/s/OVCUgcKOo1C-zbZ-Y5Roaw',
    },
    {
        'event': 'yueduyuanwen',
        'startTime': '19:00:00',
        'endTime': '24:00:00',
        'args': 'https://.....',
    },]

#从配置文件里得到事件，然后调用main执行事件
if __name__ == "__main__":
    print('打印原有events', events)
    events += parseJson()
    print('打印更新的events', events)
    main(events)