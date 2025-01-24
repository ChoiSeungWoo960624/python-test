from bs4 import BeautifulSoup 
from numpy import info
import requests

lotto_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.aslt&fbm=0&acr=1&acq=%EB%A1%9C%EB%98%90&qdt=0&ie=utf8&acir=1&query=%EB%A1%9C%EB%98%90"
res = requests.get(lotto_url)
soup = BeautifulSoup(res.text, "html.parser")

print(soup)


win_ball <= 로또번호 들어있는 정보 
