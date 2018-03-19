# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lianxi_test_ui.test1.test import add


@add
def test(driver):
    driver.get("http://www.baidu.com")
    driver.find_element('css', '#kw11').send_keys('python')

driver = webdriver.Firefox()
test(driver)

# driver = webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.get("https://mydev.100szy.com/#/login")
# driver.find_element('css', '#login_wrap > div:nth-child(3) > div:nth-child(1) > input[type="text"]').send_keys('13944096337')
# driver.find_element('css', '#login_wrap > div:nth-child(3) > div:nth-child(2) > input[type="password"]').send_keys('123456')
# driver.find_element('css', '#login_wrap > div:nth-child(3) > div:nth-child(2) > input[type="password"]').send_keys(Keys.ENTER)
# time.sleep(2)
# # driver.delete_all_cookies()
# driver.refresh()
# time.sleep(2)
# driver.delete_all_cookies()
# driver.get("https://mydev.100szy.com/#/mine/collect/0")
#
# time.sleep(2)
