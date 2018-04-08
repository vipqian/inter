import requests
import json
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/55.0.2883.87 Safari/537.36",
}


url = "http://seputu.com/"

s = requests.session()
r = s.get(url, headers=headers, verify=True)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup)
content = []
a = soup.select(" body > div.body > div:nth-of-type(9) > div > div.box > ul")
# body > div.body > div:nth-child(9)
for i in a:

    print(i)
    if "总结" in i.text:
        break

# for mulu in soup.find_all(class_='mulu'):
#     h2 = mulu.find('h2')
#     print(h2)
#     # if h2 != None:
#     #     h2_title = h2.string
#     #     list = []
#     #     for a in mulu.find(class_='box').find_all('a'):
#     #         href = a.get('href')
#     #         box_title = a.get('title')
#     #         list.append({'href': href, 'box_title': box_title})
#     #     content.append({'title': h2_title, 'content': list})
#
# for i in content:
#     print(i)
#
# # with open('qiye.json', 'wb') as fp:
# #     json.dump({'a': 'b'}, fp=fp, indent=4)





