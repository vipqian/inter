# coding=utf-8

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from interface.common.logger import logger

urllib3.disable_warnings(InsecureRequestWarning)


class HomePage():
    """商业新知首页"""
    log = logger

    def __init__(self, s):
        self.s = s

    def get_open_home(self):
        try:
            url = "http://dev.100szy.com/"
            result = self.s.get(url)
            return result.text
        except Exception as msg:
            self.log.info(str(msg))

    def get_login(self):
        try:
            url = "https://mydev.100szy.com/apipc/?v=pc1.0.0&c=user&a=is_login"
            headers = {
                "Accept": "application / json, text / plain, * / *",
                "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) " \
                                "Chrome / 64.0.3282.140Safari / 537.36",
                "Cookie": "PHPSESSID = sl79emtbo6b0091f5bshk9umj7;"
                          "referrer = http % 3A % 2F % 2Fdev.100szy.com % 2F"

            }
            r = self.s.get(url, headers=headers, verify=True)
            result = r.json()
            return result
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def login(self):
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
            return result
        except Exception as msg:
            self.log.info(str(msg))
            raise

    def tool(self):
        try:
            url = "https://api.100szy.com/index.php"

            headers = {
                "Accept": "application / json, text / plain, * / *",
                "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko)"
                                " Chrome / 64.0.3282.140Safari / 537.36",
                }

            display_data = {
                "v": "dev3.1.2",
                "a": "kjact",
                "apptype": "android",
                "c": "activity",
                "signature": "0a71f42c70cc524a27f017c61ad32910",
                "key": "6df1952c63a6db39edc3ec1bb9d3da9f",
                "token": "4822418990379df9ad0b503b458bb088",
                "timestamp": "1521797999",
                "uid": "33FC869B-6CFFDC0DC036",
                "noncestr": "ec2157b0-b459-49af-9efd-90ae4bbdd1d8",
                "only_phone_model": "ae6e80d2-50f2-4af5-8d4b-e542387fc8a1",
            }

            r = self.s.get(url, headers=headers, params=display_data, verify=True)
            print(r.url)
            print("-"*100)
            print(r.json())
        except Exception as msg:
            self.log.info(msg)

if __name__ == '__main__':
    s = requests.session()
    home = HomePage(s)
    home.get_login()
    home.login()
    home.tool()


