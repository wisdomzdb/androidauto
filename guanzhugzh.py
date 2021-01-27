import time
import random
from wechat_home import wechat_home

def guanzhugzh(d):
    wechat_home(d)
    time.sleep(1)
    d(text="微信").click()
    time.sleep(2)
    d.click(0.548, 0.076)
    time.sleep(1)
    d.click(0.841, 0.071)
    time.sleep(1)
    gzhname = open("公众号名字.txt",mode="r",encoding="utf-8").read().split("\n")
    now_line = random.randint(0, len(gzhname)-1)
    d.send_keys(gzhname[now_line], clear=True)
    time.sleep(1)
    if d(text="小程序、公众号、文章、朋友圈和表情等"):
        d(text="小程序、公众号、文章、朋友圈和表情等").click()
    else:
        d.click(0.183, 0.215)
    time.sleep(30)
    d.click(0.442, 0.31)
    time.sleep(30)
    d(text="关注").click()
    time.sleep(30)
