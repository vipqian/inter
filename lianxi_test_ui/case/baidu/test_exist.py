# coding=utf-8
"""
author:
time:
brief:
"""

import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class TestTextExist(unittest.TestCase):
    """
    判断百度中是否包换特定的字符
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @ classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def open_url(self):
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(30)
        self.driver.delete_all_cookies()

    def test_text_exist(self):
        """text is exist"""
        self.open_url()
        locator = ('css', '#u1 > a:nth-child(1)')
        text = "新闻"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    def test_text_not_exist(self):
        """text is not exist"""
        self.open_url()
        self.driver.implicitly_wait(20)
        locator = ('css', '#u1 > a:nth-child(2)')
        text = "新闻"
        result = EC.text_to_be_present_in_element(locator=locator, text_=text)(self.driver)
        self.assertFalse(result)

    def test_element_value_equality(self):
        """element values is equality"""
        self.open_url()
        locator = ('css', '#su')
        text = "百度一下"
        result = EC.text_to_be_present_in_element_value(locator=locator, text_=text)(self.driver)
        self.assertTrue(result)

    def test_element_value_not_equality(self):
        """element values is not equality"""
        self.open_url()
        locator = ('css', '#su')
        text = "百度111"
        result = EC.text_to_be_present_in_element_value(locator=locator, text_=text)(self.driver)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

