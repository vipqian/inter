"""
author:
date:
brief:
"""

import requests

class HtmlDownLoader(object):

    def download(self, url):
        if url is None:
            return None
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/55.0.2883.87 Safari/537.36"
        headers = {
            "User_Agent": user_agent
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None

    