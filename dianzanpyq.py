import time
from jinrupyq import jinrupyq

def dianzanpyq(d):
    jinrupyq(d)
    time.sleep(3)
    d(description="评论").click()
    time.sleep(1)
    if d(text="赞"):
        d(text="赞").click()
    time.sleep(1)
    