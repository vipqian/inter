import requests
import unittest
import urllib3

from interface.common.logger import logger
urllib3.disable_warnings()


class Test(unittest.TestCase):
    s = requests.session()
    log = logger

    def test_01(self):
        try:
            url = "https://mydev.100szy.com/apipc/?v=pc1.0.0&c=user&a=is_login"
            headers = {
                "Accept": "application / json, text / plain, * / *",
                "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko)"
                                " Chrome / 64.0.3282.140Safari / 537.36",
                "Cookie": "PHPSESSID=sl79emtbo6b0091f5bshk9umj7; referrer=http%3A%2F%2Fdev.100szy.com%2F"
            }

            r = self.s.get(url, headers=headers, verify=True)
            result = r.json()
            print(result)
        except Exception as msg:
            self.log.info(str(msg))
            raise

if __name__ == '__main__':
    unittest.main()