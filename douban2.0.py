from bs4 import BeautifulSoup
import requests
import re

for number in range(0,250,25):
    url = f"https://movie.douban.com/top250?start={number}"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0"
    }
    response = requests.get(url,headers=headers)
    obj = re.compile(r'<span class="title">(?P<movie_name>.*?)</span>',re.S)
    item = obj.finditer(response.text)
    for it in item:
        if re.match(r'^[\u4e00-\u9fa5]+$',it.group("movie_name")):
            print(it.group("movie_name"))
    response.close()