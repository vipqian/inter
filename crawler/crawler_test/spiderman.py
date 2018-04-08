"""
author:
brief:
date:
"""

from crawler.crawler_test.dataoutput import DataOutPut
from crawler.crawler_test.htmldownloader import HtmlDownLoader
from crawler.crawler_test.htmlparser import HtmlParser
from crawler.crawler_test.urlmanageer import UrlManager
import time


class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownLoader()
        self.parser = HtmlParser()
        self.output = DataOutPut()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            new_url = self.manager.get_new_url()
            html = self.downloader.download(new_url)
            new_urls, data = self.parser.parser(new_url, html)
            self.manager.add_new_urls(new_urls)
            self.output.store_data(data)
            print("已经抓取%s个链接" % self.manager.old_url_size())
            time.sleep(3)

        #     try:
        #         new_url = self.manager.get_new_url()
        #         html = self.downloader.download(new_url)
        #         new_urls, data = self.parser.parser(new_url, html)
        #         self.manager.add_new_urls(new_urls)
        #         self.output.store_data(data)
        #         print("已经抓取%s个链接" % self.manager.old_url_size())
        #     except Exception as msg:
        #         print("crawl failed")
        # self.output.oup_html()
        self.output.oup_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl('http://seputu.com/')
