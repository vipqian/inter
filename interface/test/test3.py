import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
# url = "http://pc-api.power.com/index.php?c=Login&a=passwordLogin"
# s = requests.session()
#
# headers = {
#     "User - Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
#     "Content-Type": "application/json;charset=utf-8"
# }
# data = {
#     "mobile": "135200000345207",
#     "password": "1111111111"
# }
#
# r = s.post(url, data=data)
#
# print(r.json())

import unittest

class Test(unittest.TestCase):

    def test(self):
        url = "http://pc-api.power.com/index.php?c=Login&a=passwordLogin"
        headers = {
            "User - Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Content-Type": "application/json;charset=utf-8"
        }
        data = {
            "mobile": "135200000345207",
            "password": "1111111111"
        }
        s = requests.session()
        r = s.post(url, data=data, verify=True)
        self.assertEqual("无效手机号", r.json()['errstr'])


if __name__ == '__main__':
    unittest.main()