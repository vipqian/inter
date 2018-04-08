from crawler.crawler_test.tet_pintu import PinTu
import json
import redis
import time

redis_client = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
now = time.strftime("%Y_%m_%d_%H_%M_%S")
file_name = now+'.html'
print(file_name)
data_str = redis_client.lpop('pintu')
data = json.loads(data_str)
print(data)
with open(file_name, 'w', encoding='utf-8') as f:
    f.writelines('<html lang="en">')
    f.writelines('<head>')
    f.writelines('<meta charset="UTF-8">')
    f.writelines('<title>Title</title>')
    f.writelines('</head>')
    f.writelines('<body>')
    f.writelines(data['title'])
    f.writelines(data['content_time'])
    f.writelines(data['brief'])
    f.writelines(data['content'])
    f.writelines('</body>')
    f.writelines('</html>')

