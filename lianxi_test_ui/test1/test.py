# coding=utf-8

__author__ = ''

from selenium import webdriver
browser = webdriver.Firefox()
browser.delete_all_cookies()

class Screenshots():
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, f):
        def inner(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except:
                import time
                now = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file("%s.jpg" % now)
                raise
        return inner

import os
import time

def add(func):

    PATH = lambda p: os.path.abspath(p)

    def wrapper(self, *args, **kwargs):
        try:
            func(self, args, kwargs)
        except AssertionError:
            path = PATH(os.getcwd() + "/screenshot")
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            os.popen("adb wait-for-device")
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
                os.makedirs(path)
            os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + timestamp + ".png"))
            os.popen("adb shell rm /data/local/tmp/tmp.png")
            # 打印出路径
            print(timestamp, '.png')
            raise

    return wrapper