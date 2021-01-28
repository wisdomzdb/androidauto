import time
import uiautomator2 as u2
from checkTime import checkTime

from guanzhugzh import guanzhugzh
from fapyq import fapyq
from pinglunpyq import pinglunpyq
from dianzanpyq import dianzanpyq
from readtxnews import ReadTXNews
from qxguanzhugzh import qxguanzhugzh
#执行事件，将事件发生
def run(d, event):
    print('设备 ', d.device_info['serial'] , ' 开始执行事件', event['event'])
    if event['event'] == 'readtxnews':
        readnews = ReadTXNews(d)
        readnews.run()
    elif event['event'] == 'dianzanpyq':
        dianzanpyq(d)
    elif event['event'] == 'fapyq':
        fapyq(d)
    elif event['event'] == 'pinglunpyq':
        pinglunpyq(d)
    elif event['event'] == 'guanzhugzh':
        guanzhugzh(d)
        print(d)
    elif event['event'] == 'qxguanzhugzh':
        qxguanzhugzh(d)
    event['times'] = event['times'] - 1

#event应该在配置文件的start和end之间发生
#判断当前时间是否在start和end之间，如果在，则有概率性发生该事件，如果发生，则返回true。
#另外需要在end之前至少发生一次，所以概率应该逐渐增大，到最后一分钟时，如果还没发生过，发生的概率应该为1，即必定返回true。
#如果发生过，应该记录下来这个事件已经发生过了，不应该再次发生。
def shouldStart(event):
    if event['times'] != 0:
        # return checkTime(event.get('startTime'), event.get('endTime'))
        return True
    return False

#main中每秒钟判断一次是否有事件该执行，如果有，则去执行事件
def loop(d, events):
    while True:
        time.sleep(10)
        for event in events:
            if shouldStart(event):
                try:
                    run(d, event)
                except:
                    pass

# TODO 这些events应该从jsonfile里读取，
# jsonfile的读取应该放到start.py里，
# main.py接收设备和事件，在设备上循环执行事件
def parseJson():
    return [{
        'event': 'dianzanpyq',
        'startTime': '10:00:00',
        'endTime': '11:00:00',
        'args': 'https://mp.weixin.qq.com/s/OVCUgcKOo1C-zbZ-Y5Roaw',
        'times':0
    },
    {
        'event': 'yueduyuanwen',
        'startTime': '10:00:00',
        'endTime': '11:00:00',
        'args': 'https://.....',
        'times':0
    },
    {
        'event': 'readtxnews',
        'startTime': '11:00:00',
        'endTime': '12:00:00',
        'args': 'https://.....',
        'times':0
    },
    {
        'event': 'fapyq',
        'startTime': '12:00:00',
        'endTime': '13:00:00',
        'args': 'https://.....',
        'times':0
    },
    {
        'event': 'guanzhugzh',
        'startTime': '12:00:00',
        'endTime': '13:00:00',
        'args': 'https://.....',
        'times':1
    },
    {
        'event': 'qxguanzhugzh',
        'startTime': '12:00:00',
        'endTime': '21:00:00',
        'args': 'https://.....',
        'times':0
    },
    {
        'event': 'pinglunpyq',
        'startTime': '13:00:00',
        'endTime': '14:00:00',
        'args': 'https://.....',
        'times':0
    }]

#从配置文件里得到事件，然后调用main执行事件
def main(dev, events):
    print('打印dev和events', dev, events)
    d = u2.connect(dev['devID'])
    events += parseJson()
    print('打印更新的events', events)
    loop(d, events)
