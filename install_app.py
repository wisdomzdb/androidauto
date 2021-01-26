import os

devices = ["566b6daf"]
apkname = "weixin7022android1820_arm64.apk"

for i in range(len(devices)):
    cmd = "adb -s " + devices[i] + " install " + apkname
    os.system(cmd)
