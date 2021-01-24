import subprocess

# 获取所有设备信息，存入到devices列表中，
# 存入3个属性，devID即序列号, devDesc为设备描述, transportID为传输ID

devices = []
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