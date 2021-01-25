import time
class OpenWeChat:
    def __init__(self, d):
        try:
            print('openwechat start')
            d.press("home")
            time.sleep(1)
            d.press("home")
            time.sleep(2)
            d(text="微信").click()
            time.sleep(5)
            while True:
                if d(text="微信") and d(text="通讯录") and d(text="发现"):
                    break
                else:
                    d.press("back")
                    time.sleep(2)
            print('openwechat end')
        except expression as identifier:
            pass