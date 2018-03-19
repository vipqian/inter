# coding=utf-8


import unittest

import requests

from common.logger import logger
from public.login import Blog


class Test(unittest.TestCase):
    log = logger

    def setUp(self):
        s = requests.session()
        self.blog = Blog(s)

    def test_login(self):
        """测试登录测试"""
        self.log.info("----start----")
        result = self.blog.login()
        self.log.info(u'调用登录结果：%s' % result)
        self.log.info(u"获取是否登录成功：%s" % result['success'])
        self.assertEqual(result['success'], True)
        self.log.info("----end----")

if __name__ == '__main__':
    unittest.main()