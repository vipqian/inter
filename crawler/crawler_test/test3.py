from basecrawler.basecrawler import BaseCrawler
from bs4 import BeautifulSoup

def get_html(url, bc):
    r = bc.requests_get(url)
    r.encoding = 'utf-8'
    return r.text



bc = BaseCrawler()
url = 'http://dev.100szy.com/cases/'
r = bc.requests_get(url)
r.encoding = 'utf-8'


soup = BeautifulSoup(r.text, 'lxml')
a = soup.select("div .search_result_item a")
urls = []
for i in a:
    urls.append(i.get('href'))
print(urls)

for url in urls:
    bc.requests_get(url)
