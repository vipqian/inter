# coding=utf-8
"""
author:fei
date:
brief:
"""


import requests
import re
import urllib3

from interface.common.logger import logger

from urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
# urllib3.disable_warnings(InsecureRequestWarning)


class Blog():
    log = logger

    def __init__(self, s):              #全局参数
        self.s = s

    def login(self):
        try:
            url = "https://passport.cnblogs.com/user/signin"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/json; charset=utf-8",
                "X-Requested-With": "XMLHttpRequest",
                "Cookie": "_ga=GA1.2.584042726.1499410300; pgv_pvi=5428108288; _gid=GA1.2.1724566868.1502074838;"
                          "SERVERID=dcc5cb8c464da84cc9928c22dd5884f8|1502155777|1502155717;"
                          " _gat=1Connection: keep-alive",
                "Connection": "keep-alive"
            }
            payload = {
                "input1": "P64dyz0cQrZCd+kZRLE06t+cncDCOcFHnMzW5onpjTANsAtnrXYOxwUUl28xM/5HiH77RtdQuz1hGF6VhLif/n8BVJOU"
                          "ZSgQtm/ckuy9fXqKg87lhqJgySAhNBzobUTtP5TfJBEXFEirEOwbs96rzJVm5vnVCyn5s5h+obHhHxw=",
                "input2": "H+R9TCYu0AiCw5/Yg7Jc0Na3ONqCnSZ8qSuIoPYroP1QmO+9ptTFAhCNesQXB86Syl0B6Rv/Xb0OPe4EHya5Fb6btCAX"
                          "SnsCuwJMw6DFt93CE5PZLhg9x+hxecehxO5phFEyCfPUijwo9UqRBGRpiHMkPegFFV9pZYQOH1Y4vDg=",
                "remember": False
            }
            r = self.s.post(url, headers=headers, json=payload)
            self.s.close()
            return r.json()
        except Exception as msg:
            self.log.info(str(msg))
    # def save(self, title, body):
    #     """保存到草稿箱：
    #     参数1：title：标题
    #     参数2：body：内容"""
    #     url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    #     d = {
    #         "__VIEWSTATE": "",
    #         "__VIEWSTATEGENERATOR": "FE27D343",
    #         "Editor$Edit$txbTitle": title,
    #         "Editor$Edit$EditorBody": body,
    #         "Editor$Edit$Advanced$ckbPublished": "on",
    #         "Editor$Edit$Advanced$chkDisplayHomePage": "on",
    #         "Editor$Edit$Advanced$chkComments": "on",
    #         "Editor$Edit$Advanced$chkMainSyndication": 'on',
    #         "Editor$Edit$Advanced$txbEntryName": "",
    #         "Editor$Edit$Advanced$txbExcerpt": "",
    #         "Editor$Edit$Advanced$txbTag": "",
    #         "Editor$Edit$Advanced$tbEnryPassword": '',
    #         "Editor$Edit$lkbDraft": u"存为草稿"
    #     }
    #     r2 = self.s.post(url2, data=d)
    #     self.s.close()
    #     print(r2.url)
    #     return r2.url
    #
    #
    # def get_postid(self, r2_url):
    #     """获取postid"""
    #     postid = re.findall(r"postid=(.+?)&", r2_url,)
    #     print(postid[0])
    #     return postid[0]
    #
    # def del_tie(self, postid):
    #     url3 = "https://i.cnblogs.com/post/delete"
    #     json_data ={"postId": postid}
    #     r3 = self.s.post(url3, json=json_data)
    #     self.s.close()
    #     print(r3.json())
    #     return r3.json()


if __name__ == '__main__':
    s = requests.session()
    Blog(s).login()
    # u = Blog(s).save("titl3e133322", "sdfjas")
    # pid = Blog(s).get_postid(u)
    # result = Blog(s).del_tie(pid)
    # print(result)