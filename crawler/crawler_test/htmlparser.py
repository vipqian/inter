"""
author:
date:
brief:
"""

import re
from bs4 import BeautifulSoup
import urllib.parse

class HtmlParser(object):

    def parser(self, page_url, html_cont):
        """
        用于网页解析，返回url和数据
        :param page_url:
        :param html_cont:
        :return:
        """
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_url = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_url, new_data

    def _get_new_urls(self, page_url, soup):
        """
        获取新的url集合
        :param page_url:
        :param soup:
        :return:
        """
        new_urls = set()
        # links = soup.find_all('a', href=re.compile(r'/view/\d+\.html'))
        links = soup.find_all('a', href=re.compile(r'/zanghaihua/\d+\.html'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            # print(new_urls)

        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        获取有效的数据
        :param page_url:
        :param soup:
        :return:
        """
        data = {}
        data['url'] = page_url
        for mulu in soup.find_all(class_='mulu'):
            h2 = mulu.find('h2')
            if h2 != None:
                h2_title = h2.string
                for i in mulu.find(class_='box').find_all('a'):
                    data['title'] = i.get_text()
                    data['href'] = i.get('href')
        return data



