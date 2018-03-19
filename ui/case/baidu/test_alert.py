# coding=utf-8
"""
author:
time:
brief:
"""

import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from ui.common.loger import logger



class TestAlert(unittest.TestCase):
    """
    判断是否有alert弹窗
    """
    @classmethod
    def setUpClass(cls):
        cls.log = logger
        cls.driver = webdriver.Firefox()
        cls.log.info('测试开始')

    @classmethod
    def tearDownClass(cls):
        cls.log.info('测试结束')
        cls.driver.quit()

    def set_search(self):
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(30)
        mouse = self.driver.find_element("css", "#u1 > a.pf")
        ActionChains(self.driver).move_to_element(mouse).perform()
        self.driver.find_element('css', '#wrapper > div.bdpfmenu > a.setpref').click()
        s = self.driver.find_element('css', '#nr')
        Select(s).select_by_index(1)
        js = 'document.querySelector("#gxszButton > a.prefpanelgo").click()'
        self.driver.execute_script(js)

    def test_alert_exist(self):
        self.set_search()
        result = EC.alert_is_present()(self.driver)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
