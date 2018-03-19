# coding=utf-8

import unittest
from common.logger import logger
import os


class TestAdd(unittest.TestCase):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    log = logger

    def test_add(self):
        self.log.info("-----test start add ------")
        self.assertEqual((5+3), 8)
        self.log.info("-----test end add---------")

if __name__ == '__main__':
    unittest.main()
