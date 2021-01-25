import time
from openWeChat import OpenWeChat

class ReadTXNews:
    def __init__(self, d):
        OpenWeChat(d)
        self.d = d
    def run(self):
        while True:
            if self.d(text="腾讯新闻"):
                break
            else:
                self.d.swipe_ext("up", 0.6)
                time.sleep(1)
        self.d(text="腾讯新闻").click()
        time.sleep(1)
        self.d.click(0.646, 0.906)
        time.sleep(2)
        for i in range(4):
            self.d.swipe_ext("up", 0.6)
            time.sleep(5)
        self.d.press("back")
        time.sleep(1)
        self.d.press("back")