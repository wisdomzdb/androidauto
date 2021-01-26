import time
import random
from jinrupyq import jinrupyq


def fapyq(d):
    jinrupyq(d)
    time.sleep(2)
    d.long_click(0.925, 0.071, 0.7)
    time.sleep(1)
    pyq_fi = open("朋友圈文案.txt",mode="r",encoding="utf-8").read().split("\n")
    now_line = random.randint(0, len(pyq_fi)-1)
    d.send_keys(pyq_fi[now_line], clear=True)
    time.sleep(1)
    d(text="发表").click()