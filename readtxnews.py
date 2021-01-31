import time
import random
from checkxiaoxi import checkxiaoxi

def readtxnews(d): # 阅读腾讯新闻
    if checkxiaoxi(d):
        d(text="微信").double_click()
        time.sleep(2)
        while True:
            if d(resourceId="com.tencent.mm:id/ga3"):
                d(resourceId="com.tencent.mm:id/ga3").click()
                time.sleep(2)
                break
            else:
                d.swipe_ext("up", 0.6)
                time.sleep(2)
        if d(text="腾讯新闻"):
            if d(resourceId="com.tencent.mm:id/gd2"):
                d(resourceId="com.tencent.mm:id/gd2").click()
            else:
                d.click(0.482, 0.563)
        time.sleep(2)
        for i in range(6):
            d.swipe_ext("up", 0.6)
            time.sleep(random.randint(4,8))
        d.press("back")
        time.sleep(1)


        