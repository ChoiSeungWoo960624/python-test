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

html_url = "https://finance.naver.com/item/main.naver?code=005930"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")

#주식명
title = soup.select_one("h2")
print (f"주식명 : {title.text}")


#가격
mone = soup.select_one(".no_today .no_up .blind") 
#.no_today .no_up 했을 때 숫자가 중복이 일어나는건 .no_up출력시 중복 하위 요소의 텍스트(.blind)가 합쳐져서그렇다. 
print(f"가격 : {mone.text}원")

'''
#전일 대비 //구현을 못하겠음
rising_day = soup.select_one(".rate_info .today .no_exday")
mount_day = soup.select_one(".no_up .ico up .blind")
print(f"{rising_day} 전월 대비 : {mount_day}")
'''

#그래프 
graph_today = soup.select_one("#img_chart_area")
if graph_today:
    print(f"그래프: {graph_today['src']}")