from basecrawler.basecrawler import BaseCrawler, BeautifulSoup
import redis

redis_client = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

import json
url = "http://dev.100szy.com/cases/577877/"
bc = BaseCrawler()
r = bc.requests_get(url)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup)
each = soup.select("div .article_title > h2")[0]
title = each.text
each = soup.select("div .article_tip")[0]
time = bc.datetime_format(each.text)
each = soup.select('div .article_content')[0]
content = each.prettify()
data = {"title": title, "time": time, "content": content}

data_str = json.dumps(data)
# redis_client.lpush("abc", data_str)
# redis_client.sadd("bcd", data_str)
redis_client.hset("bcd", "url", data_str)
ss = redis_client.hget('bcd', 'url')
data = json.loads(ss)
print(data["content"])


