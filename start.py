import subprocess
from multiprocessing import Process
from main import main

devices = []

# 获取所有设备信息，存入到devices列表中，
# 存入3个属性，devID即序列号, devDesc为设备描述, transportID为传输ID
def getDevices():
    try:
        cmd = 'adb devices -l'
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in res.stdout.readlines():
            index = line.find(b'device product')
            if index > 0:
                info = line.split(sep=b':')
                devID = info[0].split()[0].decode()
                devDesc = (info[1] + info[2] + info[3].split()[0]).decode()
                transportID = int(info[4].split(b'\r\n')[0].decode())
                dev = {'devID': devID, 'devDesc': devDesc, 'transportID': transportID}
                devices.append(dev)
        print(devices)
        res.stdout.close()
    except expression as identifier:
        pass

events = [{
        'event': 'faPengyouquan',
        'startTime': '00:00:00',
        'endTime': '00:10:00',
        'args': './发朋友圈圈素材/素材8号.txt',
    },]

def task(dev):
    main(dev, events)

# 为每一个设备启动一个子进程，使用子进程执行各个设备的脚本
def start():
    for dev in devices:
        p = Process(target=task, args=(dev,), name="gzh-dev-" + dev['devID'])
        p.start()
    p.join()

if __name__ == '__main__':
    getDevices()
    start()