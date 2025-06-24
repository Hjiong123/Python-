from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0"
}
for star_num in range(0,250,25):
    response = requests.get(f"https://movie.douban.com/top250?start={star_num}",headers=headers)
    html = response.text
    soup = BeautifulSoup(html)
    all_title = soup.findAll("span",attrs = {"class":"title"})
    for title in all_title:
        title_useful = title.string
        if "/" not in title.string:
            print(title.string)