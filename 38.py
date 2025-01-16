from bs4 import BeautifulSoup 
import requests


'''
#서울시청 웹크롤링
html_url = "https://www.seoul.go.kr/main/index.jsp"
res = requests.get(html_url)
#print(res.text)
soup = BeautifulSoup(res.text, "html.parser")
print(soup)

all_nav = soup.select("nav > ul > li > a")
print(all_nav)
for i in all_nav:
    print(i.text)
'''

html_ur2 = "https://www.museum.go.kr/site/main/content/tour_guidance"
res = requests.get(html_ur2)
soup = BeautifulSoup(res.text, "html.parser")
all_nav = soup.select("div.page-content-type1 > ul.display-content-area > li > ul.display-content:first-child")
#print(all_nav)
for i in all_nav:
    print(i.text)