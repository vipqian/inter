import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/55.0.2883.87 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

url = "http://seputu.com/biji1/1.html"

r = requests.get(url, headers=headers, verify=True)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, 'lxml')
res = ""
with open("1.html", 'w', encoding='utf-8') as f:
    f.writelines("<html>")
    for node_title in soup.select("body > div.body > div.bg > h1"):
        f.writelines("%s \n" % node_title.text)
    for node_brief in soup.select('div.mark'):
        f.writelines('%s \n' % node_brief.text)
    # for node_p in soup.select('div.content-body'):
    #     # print(node_p.prettify())
    #     res = re.sub(r"<script>.*?</script>","", node_p.prettify(), flags=re.S)
    #     res = re.sub("<.*?>", "", res, flags=re.S)
    #     res = re.sub(r"www.seputu.com", "", res, flags=re.S)
    #     res = re.sub(r"http://seputu.com/", "", res, flags=re.S)


        # f.writelines('%s \n' % res.strip())
    res = soup.select('div.content-body')[0].prettify()
    res = re.sub(r"<script>.*?</script>", "", res, flags=re.S)
    # res = re.sub("<.*?>", "", res, flags=re.S)
    res = re.sub(r"www.seputu.com", "", res, flags=re.S)
    res = re.sub(r"http://seputu.com/", "", res, flags=re.S)
    res = re.sub(r"\n", "", res, flags=re.S)
    res = re.sub(r'', '', res, flags=re.S)
    print(res)
    f.writelines('%s \n' % res.strip())
    f.writelines('</html>')

# titles = soup.find_all(class_='bg')
# for i in titles:
#     if i != None:
#         print(i.find('h1'))