# coding=utf-8


import unittest

import requests

from interface.common.logger import logger
from interface.page.login import Blog


class Test(unittest.TestCase):
    log = logger

    def setUp(self):
        s = requests.session()
        self.blog = Blog(s)

    def test_login(self):
        """测试登录测试"""
        try:
            result = self.blog.login()
            self.assertTrue(result['success'])
        except Exception as msg:
            self.log.info(str(msg))
            raise

if __name__ == '__main__':
    unittest.main()