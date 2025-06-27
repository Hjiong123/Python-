import requests
from bs4 import BeautifulSoup
import re


url = "https://www.dytt8899.com/"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0"
}
response = requests.get(url,headers=headers)
response.encoding = "gbk"
html = response.text
print(response.status_code)
obj = re.compile(r'2025必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj1 = re.compile(r"<li>.*?'(?P<www>.*?)'.*?《(?P<movie_name>.*?)》.*?</li>")
ul = obj.finditer(html)
f = open("movie_file",'a',encoding="utf-8")
for it in ul:
    movie = obj1.finditer(it.group("ul"))
    for item in movie:
        www = item.group("www")
        movie_name = item.group("movie_name")
        str = f"电影名字是：{movie_name},网址是：https://www.dytt8899.com/{www}\n"
        f.write(str)
f.close()
response.close()