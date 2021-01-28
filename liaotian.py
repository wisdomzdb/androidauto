import time
from checkxiaoxi import checkxiaoxi

def recallxiaoxi(d):
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
            d.press("back")
        else:
            d.press("back")