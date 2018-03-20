# coding=utf-8
"""
author:
time:
brief
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from ui.common.log import logger

log = logger
log.info('测试开始')

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
# WebDriverWait(driver, 10, 1).until(lambda x: x.find_element('css', '#u1 > a.pf'))

def elements(locator, timeout=10):
    element = WebDriverWait(browser, timeout, 1).until(lambda x: x.find_element(*locator))
    return element
set_locator = ('css', '#u1 > a.pf')
search_locator = ('css', '#wrapper > div.bdpfmenu > a.setpref')
set_element = elements(set_locator)
ActionChains(browser).move_to_element(set_element).perform()
search = elements(search_locator)
search.click()
select_locator = ('css', '#nr')
select = elements(select_locator)
Select(select).select_by_index(1)
js = 'document.querySelector("#gxszButton > a.prefpanelgo").click()'
browser.execute_script(js)
if EC.alert_is_present()(browser):
    print("保存成功")
else:
    print("保存失败")
t = browser.switch_to_alert()
t.accept()
browser.quit()
log.info('测试结束')


