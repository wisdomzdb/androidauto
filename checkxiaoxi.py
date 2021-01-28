import time
from wechat_home import wechat_home

def checkxiaoxi(d):
    wechat_home(d)
    time.sleep(2)
    if d(resourceId="com.tencent.mm:id/gik"):
        return True
    return False