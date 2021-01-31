import time
import random
from wechat_home import wechat_home

def find_essayqun(d): # 寻找文章群
    wechat_home(d)
    time.sleep(2)
    d(text="微信").double_click()
    time.sleep(2)
    while True:
        if d(text="文章群"):
            d(text="文章群").click()
            time.sleep(3)
            break
        else:
            d.swipe_ext("up",0.7)
            time.sleep(2)

def enter_essay(d,essay_name): # 进入文章
    find_essayqun(d)
    time.sleep(2)
    while True:
        if d(text=essay_name):
            d(text=essay_name).click()
            break
        else:
            d.swipe_ext("down",0.6)
            time.sleep(2)

def yueduwenzhang(d,essay_name): # 阅读文章
    enter_essay(d,essay_name)
    time.sleep(10)
    while 10:
        d.swipe_ext("up",0.6)
        time.sleep(random.randint(8,16))
    

    
