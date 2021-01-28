import random
import time
import xlrd
import xlwt
import uiautomator2 as u2

def twophoneschat(d):
devices = ["9674c2e8"]
wxname = []
d = [d,[]]
namei = 0

fi = xlrd.open_workbook(r'手机信息.xlsx')
sheet1 = fi.sheet_by_name('Sheet1')

def inchat(aid_name,d):
    d.press("home")
    time.sleep(1)
    d(text="微信").click()
    time.sleep(2)
    d.click(0.382, 0.957)
    time.sleep(1)
    while True:
        if d(text=aid_name):
            d(text=aid_name).click()
            time.sleep(1)
            d(text="发消息").click()
            break
        else:
            d.swipe_ext("up", 0.6)
            time.sleep(2)

def sendkeys(d,chatfile):
    d.click(0.313, 0.972)
    d.send_keys(chatfile, clear=True)
    time.sleep(1)
    d(text="发送").click()

while True:
    try:
        if str(int(sheet1.cell(namei,1).value)) == devices[0]:
            wxname.append(sheet1.cell(namei,6).value)
            break
        else:
            namei = namei + 1
    except:
        if sheet1.cell(namei,1).value == devices[0]:
            wxname.append(sheet1.cell(namei,6).value)
            break
        else:
            namei = namei + 1
        
aid = random.randint(1,4)
while True:
    try:
        if str(int(sheet1.cell(aid,1).value)) == devices[0]:
            aid = random.randint(1,4)
        else:
            wxname.append(sheet1.cell(aid,6).value)
            devices.append(str(int(sheet1.cell(aid,1).value)))
            break
    except:
        if sheet1.cell(aid,1).value == devices[0]:
            aid = random.randint(1,4)
        else:
            wxname.append(sheet1.cell(aid,6).value)
            devices.append(sheet1.cell(aid,1).value)
            break

d[0] = u2.connect(devices[0])
d[1] = u2.connect(devices[1])

inchat(wxname[1],d[0])
inchat(wxname[0],d[1])


wx_fi = open("微信常用聊天语言.txt",mode="r",encoding="utf-8").read().split("\n")
now_line = random.randint(1, 108)
while True:
    if wx_fi[now_line] == "----------------------------------------":
        while True:
            now_line = now_line + 1
            if wx_fi[now_line] == "----------------------------------------":
                break
            else:
                chatfile = wx_fi[now_line].split("：")[1]
            if wx_fi[now_line].split("：")[0] == "A":
                sendkeys(d[0],chatfile)
            elif wx_fi[now_line].split("：")[0] == "B":
                sendkeys(d[1],chatfile)
            time.sleep(random.randint(3, 34))
    else:
        now_line = now_line - 1
        continue
    break
for i in range(2):
    d[0].press("back")
    d[1].press("back")