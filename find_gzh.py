import time
from wechat_home import wechat_home
def find_gzh(gzh_name,d):
    wechat_home(d)
    time.sleep(1)
    d(text="通讯录").click()
    time.sleep(2)
    d(text="公众号").click()
    time.sleep(3)
    while True:
        if  d(text=gzh_name):
            d(text=gzh_name).click()
            break
        else:
            d.swipe("up", 0.6)
            time.sleep(2)
