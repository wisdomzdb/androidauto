import time
import random
from jinrupyq import jinrupyq

def pinglunpyq(d): # 评论朋友圈
    jinrupyq(d)
    time.sleep(2)
    d(description="评论").click()
    time.sleep(1)
    if d(text="评论"):
        d(text="评论").click()
        time.sleep(1)
        d.click(0.287, 0.915)
        time.sleep(1)
        comments = open("评论朋友圈.txt",mode="r",encoding="utf-8").read().split("\n")
        now_line = random.randint(0, len(comments)-1)
        d.send_keys(comments[now_line], clear=True)
        time.sleep(1)
        d(text="发送").click()
        time.sleep(1)