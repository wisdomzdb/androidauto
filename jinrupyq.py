import time
from wechat_home import wechat_home

def jinrupyq(d): # 进入朋友圈
    wechat_home(d)
    time.sleep(2)
    d(text="发现").click()
    time.sleep(1)
    d(text="朋友圈").click()