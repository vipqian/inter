from basecrawler.basecrawler import BaseCrawler, BeautifulSoup
import redis

class Crawler(BaseCrawler):

    def __init__(self):
        self.mysql_client = "123"
        super(Crawler, self).__init__()


    def run(self):
        rule = redis.pop("url")
        url = rule["url"]

        resp = self.requests_get(url)
        soup = BeautifulSoup(resp.text, 'lxml')
        urls = self.get_content_urls(soup, rule)
        for url in urls:
            resp = self.requests_get(url)
            soup = BeautifulSoup(resp.text, 'lxml')
            data = self.get_content(soup)
            self.save_data(data)


    def get_content_urls(self, soup, rule):
        soup.select(rule["list_url_css"])
        return ["url1"]

    def get_content(self, soup, rule):
        return {"title":"123", "content":"123"}

    def save_data(self, data):
        sql = "insert into table_name (fields)values(values)";
        self.mysql_client.exec(sql)
        self.mysql_client.commit()
