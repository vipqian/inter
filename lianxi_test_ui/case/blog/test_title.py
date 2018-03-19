# coding=utf-8
"""
author:
time:
brief:
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestBlogTitle(unittest.TestCase):
    """
    判断title是否正确
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def open_url(self):
        self.driver.get("http://www.cnblogs.com/yoyoketang")
        self.driver.implicitly_wait(30)

    def test_title(self):
        """
        判断title是否完全相等
        :return:
        """
        self.open_url()
        title = EC.title_is("上海-悠悠 - 博客园")
        self.assertTrue(title(self.driver))

    def test_title_contains(self):
        """
        判断title是否包含指定字符
        :return:
        """
        self.open_url()
        title = EC.title_contains("上海")
        self.assertTrue(title(self.driver))


if __name__ == '__main__':
    unittest.main()
