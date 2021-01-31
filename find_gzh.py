import time
from wechat_home import wechat_home

def find_gzh(d,gzh_name): # 寻找公众号
    wechat_home(d)
    time.sleep(1)
    d(text="通讯录").double_click()
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
