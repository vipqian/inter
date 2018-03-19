# coding=utf-8
"""
author:
date:
brief:
"""

import unittest
from page.login_page import LoginPage, browser, login_url
from common.readexcel import ReadExcel
import ddt
from common.log import logger

excelpath = r"F:\F_lianxi\lianxi_test_ui\common\password.xlsx"
sheet = "Sheet1"
data = ReadExcel(excelpath, sheet).data_list()


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.browser = LoginPage(cls.driver)
        cls.log = logger
        cls.log.info('测试开始')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        cls.log.info('测试结束')

    def setUp(self):
        # self.driver = browser()
        # self.browser = LoginPage(self.driver)
        self.browser.open_url(login_url)
        self.browser.refresh()

    def tearDown(self):
        # self.browser.quit()
        pass

    def login_case(self, name, password):
        self.browser.input_name(name)
        self.browser.input_password(password)
        self.browser.click_login_button()

    @ddt.data(*data)
    def test_login_success(self, data):
        try:
            self.log.info('测试的数据为：%s' % str(data))
            self.login_case(str(int(data['name'])), str(int(data['password'])))
            print(str(int(data['name'])), str(int(data['password'])))
            homen_element = ('css', '#header > div > nav > ul > li:nth-child(1) > a')
            if self.browser.find_element(homen_element):
                result = True
            else:
                result = False

            if int(data['result']):
                self.assertTrue(result)
            else:
                self.assertFalse(result)
        except Exception as msg:
            self.log.info('错误信息为:%s' % str(msg))
            raise

    def test_click_remember(self):
        try:

            self.browser.click_register()
            locator = ('css', '#reg_wrap > div.loginTitle > span:nth-child(1)')
            text = self.browser.get_text(locator)
            self.assertEqual('手机注册', text)
        except Exception as msg:
            self.log.info('错误信息为:%s' % str(msg))
            raise

if __name__ == '__main__':
    unittest.main()



