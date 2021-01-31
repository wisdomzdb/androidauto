import time
from wechat_home import wechat_home
import random

def qxguanzhugzh(d): # 随机取消关注公众号
    wechat_home(d)
    time.sleep(1)
    d(text="通讯录").click()
    time.sleep(1)
    d(text="公众号").click()
    time.sleep(2)
   
    while True:
        gzhname = open("公众号名字.txt",mode="r",encoding="utf-8").read().split("\n")
        now_line = random.randint(0, len(gzhname)-1)
        num = 0
        for i in range(4):
            if d(text=gzhname[now_line]):
                d(text=gzhname[now_line]).long_click(1.5)
                break
            else:
                d.swipe_ext("up", 0.65)
                num = num + 1
                time.sleep(2)
        if num < 4:
            break
    time.sleep(1)
    d(text="不再关注").click()
    time.sleep(2)
    d(text="不再关注").click()
    time.sleep(1)

        
            
