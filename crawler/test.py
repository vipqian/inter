from basecrawler.basecrawler import BaseCrawler
from bs4 import BeautifulSoup

url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&oq=diva&rsv_pq=ca6ae15a00003b7f&rsv_t=f3eea74eHoGGjltjHnry4TWUTRNnM5FW0h2HQ3Bt1%2B%2B6UWqYPlp%2FTBrmZuM&rqlang=cn&rsv_enter=1&rsv_sug3=29&rsv_sug1=28&rsv_sug7=100&rsv_sug2=0&inputT=1284623&rsv_sug4=1284776&rsv_sug=2"

bc = BaseCrawler()

res = bc.requests_get(url)


soup = BeautifulSoup(res.text, 'lxml')

for node_a in soup.select("div h3.t"):
    print(node_a.text)