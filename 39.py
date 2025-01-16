#kbs 뉴스 크롤링
from bs4 import BeautifulSoup
import requests

"""
html_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8153501"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

# 제목
title = soup.select_one(".headline-title")
print("제목 : ", title.text.strip())

# 내용
content = soup.select_one("#cont_newstext")
print("내용 : ", content.text.strip())

with open("news.txt", "w", encoding="utf-8") as file:
    file.write(title.text.strip() + "\n")
    file.write(content.text.strip())
"""
#명언 크롤링
html_url = "https://quotes.toscrape.com/page/2/"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, "html.parser")
quote = soup.select(".quote > span.text")  # 명언내용
# print(quote)
# for i in quote:
#     print(i.text.strip())
text = [i.text.strip() for i in quote]
# print(text)
# print(len(text))

speaker = soup.select(".quote .author")
# print(speaker)
author = [i.text.strip() for i in speaker]
# print(len(author))
zipped = list(zip(text, author))
for text, speak in zipped:
    print(f"명언자: {speak} \n내용: {text}")