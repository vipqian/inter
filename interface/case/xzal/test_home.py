# coding=utf-8

import requests
import unittest
import urllib3
from interface.common.logger import logger
from urllib3.exceptions import InsecureRequestWarning

from interface.page.home import HomePage
urllib3.disable_warnings(InsecureRequestWarning)


class Home(unittest.TestCase):
    log = logger
    s = requests.session()

    def test_home(self):
        try:
            result = HomePage(self.s).get_open_home()
            self.assertIn('分页猜你喜欢的数据', result)
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def test_get_login(self):
        try:
            result = HomePage(self.s).get_login()
            self.assertTrue(result['info'])
        except Exception as msg:
            self.log.info(str(msg))
            raise

if __name__ == '__main__':
    unittest.main()