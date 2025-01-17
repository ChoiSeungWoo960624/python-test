# 환율정보 크롤링하기기
from os import name
from bs4 import BeautifulSoup
import requests


html_url = "https://finance.naver.com/marketindex/"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")
'''
#미국달러
date1 = soup.select_one(".value")
name1 = soup.select_one("h3.h_lst")
print(name1.text.strip(), date1.text.strip())


#일본엔화
date2 = soup.select_one(".jpy .head_info .value")
nate2 = soup.select_one(".jpy .h_lst")
print(nate2.text, date2.text)
'''
#유럽eur
date3 = soup.select_one("")
name3 = soup.select_one(".eur .h_lst")
print(name3.text)

#중국cny
date1 = soup.select_one(".head_info")
name1 = soup.select_one(".h_lst")
print(f"{name1} {date1}")
