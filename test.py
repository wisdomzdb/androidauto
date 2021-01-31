import uiautomator2 as u2
import time
import random

d = u2.connect("657bcc25")

def wechat_home(d):
    d.press("home")
    time.sleep(1)
    d.press("home")
    time.sleep(2)
    d(text="微信").click()
    time.sleep(5)
    while True:
        if d(text="微信") and d(text="通讯录") and d(text="发现"):
            break
        else:
            d.press("back")
            time.sleep(2)


def find_gzh(d,gzh_name):
    wechat_home(d)
    time.sleep(1)
    d(text="通讯录").click()
    d(text="通讯录").click()
    time.sleep(2)
    d(text="公众号").click()
    time.sleep(3)
    while True:
        if  d(text=gzh_name):
            d(text=gzh_name).click()
            break
        else:
            d.swipe_ext("up", 0.7)
            time.sleep(2)

def yueduwenzhang(d,gzh_name,essay_name):
    find_gzh(d,gzh_name)
    time.sleep(2)
    d.click(0.928, 0.069)
    time.sleep(2)
    while True:
        if d(text=essay_name):
            d(text=essay_name).click()
            time.sleep(10)
            break
        else:
            d.swipe_ext("up", 0.7)
            time.sleep(2)
    while 10:
        d.swipe_ext("up", 0.7)
        time.sleep(random.randint(8,16))
        
        
yueduwenzhang(d,"大江英语","初中英语冠词易错陷阱完全归纳")