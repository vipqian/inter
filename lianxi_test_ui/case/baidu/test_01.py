# coding=utf-8
"""
author:
date:
brief:测试打开网页
"""
import unittest
from selenium import webdriver


class TestTitle(unittest.TestCase):
    """
    打开百度，查看title是否为打开页面的title
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_title(self):
        """打开百度，查看title是否为打开页面的title"""
        self.driver.get("http://www.baidu.com")
        title = self.driver.title
        self.assertEqual("百度一下，你就知道", title)


if __name__ == '__main__':
    unittest.main()

