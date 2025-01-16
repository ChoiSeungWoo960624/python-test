'''
#뉴스 크롤링
from bs4 import BeautifulSoup
import requests


html_url = "https://n.news.naver.com/mnews/article/015/0005083247?sid=101"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

# 제목
title = soup.select_one("#title_area")
all_nav = soup.select("div > h2 id > span")
print("제목 : ", title.text.strip())


#발행일
date = soup.select_one(".media_end_head_info_datestamp_time")
all_nav = soup.select("div > em > span")
print("발행일 : ", date.text.strip())


# 내용
content = soup.select_one("#dic_area")
print("내용 : ", content.text.strip())
'''

'''
# 환율정보 크롤링하기기
from bs4 import BeautifulSoup
import requests


html_url = "https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_USDKRW"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

#미장 환율율
date1 = soup.select_one(".head_info")
all_nav = soup.select("div > span")
print(date1.text.strip())
#미장 정보
name1 = soup.select_one(".h_lst")
all_nav = soup.select("href > h3")
print(name1.text.strip())
'''

#주식정보 크롤링하기
from bs4 import BeautifulSoup
import requests

html_url = "https://m.stock.naver.com/worldstock/stock/KO/total"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

#주식 이름
title = soup.select_one("span.GraphMain_name__cEsOs")
all_nav = soup.select("div > span")
print("제목 : ", title.text.strip())

#가격
mone = soup.select_one(".GraphMain_price__H72B2")
all_nav = soup.select("strong > span")
print("가격 : ", mone.text.strip())

#전월 대비 
previous_month = soup.select_one(".VGap_gap__LQYpL2")
all_nav = soup.select("div > span")
print("전월 대비 : ", previous_month.text.strip())