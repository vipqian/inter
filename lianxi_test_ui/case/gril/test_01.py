from common.find_element import FindElement, browser
from selenium import webdriver
import unittest
from common.log import logger


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = logger
        cls.logger.info('开始测试')

    @classmethod
    def tearDownClass(cls):
        cls.logger.info('测试结束')

    def test(self):
        try:
            self.assertTrue(False)
        except Exception as msg:
            self.logger.info(msg)
            raise

    def test_01(self):
        try:
            self.assertTrue(True)
        except Exception as msg:
            self.logger.info(msg)
            raise

if __name__ == '__main__':
    unittest.main()