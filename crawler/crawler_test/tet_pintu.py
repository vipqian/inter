from basecrawler.basecrawler import BaseCrawler, BeautifulSoup
import json
import redis


class PinTu(BaseCrawler):

    def __init__(self):
        self.redis_client = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
        super(PinTu, self).__init__()

    def run(self, url):
        urls = self.get_content_urls(url)
        dataset = self.get_content(urls)
        self.save_data(dataset)

    def get_content_urls(self, url):
        bc = BaseCrawler()
        r = bc.requests_get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        each = soup.select("div .article-text h2 a")
        urls = []
        for i in each:
            get_url = bc.get_full_url(url, i['href'])
            urls.append(get_url)
        return urls

    def get_content(self, urls):
        lis = []
        for url in urls:
            print(url)
            r = self.requests_get(url)
            soup = BeautifulSoup(r.text, 'lxml')
            title = soup.select('.article-title-and-type h1')[0].prettify()
            content_time = self.datetime_format(soup.select(".article-date span")[0].prettify())
            brief = soup.select("#note")[0].prettify()
            content = soup.select('.mixin-article-v3')[0].prettify()
            data = {'title': title, 'content_time': content_time, 'brief': brief, 'content': content}
            data_str = json.dumps(data)
            lis.append(data_str)
        return lis

    def save_data(self, dataset):
        for data in dataset:
            self.redis_client.sadd('pintu2', data)


if __name__ == '__main__':

    pt = PinTu()
    url = "https://www.pintu360.com/"
    pt.run(url)
