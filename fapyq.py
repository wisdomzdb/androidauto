import time
import random
from jinrupyq import jinrupyq

def fapyq(d): # 发朋友圈
    jinrupyq(d)
    time.sleep(2)
    d.long_click(0.925, 0.071, 1)
    time.sleep(1)
    try:
        pyq_fi = open("朋友圈文案.txt",mode="r",encoding="utf-8").read().split("\n")
        now_line = random.randint(1, len(pyq_fi)-1)
        d.send_keys(pyq_fi[now_line], clear=True)
        time.sleep(2)
        d(text="发表").click()
        time.sleep(2)
    except:
        d.press("back")
        time.sleep(2)
        d(text="退出").click()
        time.sleep(1)
    