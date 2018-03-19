# coding=utf-8
"""
@author:
@time:
@file:
"""

import unittest
import ddt
import time
from common.readexcel import ReadExcel

excelpath = r"F:\F_lianxi\lianxi_test_ui\common\password.xlsx"
sheet = "Sheet1"
data = ReadExcel(excelpath, sheet).data_list()


@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        time.sleep(1)
        print('start')

    def tearDown(self):
        time.sleep(1)
        print("end")

    @ddt.data(*data)
    def test_01(self, date):
        print(date)

if __name__ == '__main__':
    unittest.main()
