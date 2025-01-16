from bs4 import BeautifulSoup


html_str = """
<html>
    <body>
        <div id="content">
            <u1 class="industry">
             <li>인공지능</li>
             <li>빅데이터</li>
             <li>스마트팩토리</li>
            </ul>
            <ul classs="language"
             <li>Python</li>
             <li>C++</li>
             <li>Javascript</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_str, "html.parser")
print(soup)

# lxml => 속도가 빠름. pip install lxml설치필요
# html5lib => 속도느림. pip install html5lib. html5규격을 엄격

first_ul = soup.find("ul")
print(first_ul)
print(first_ul.text) # 테그없이 텍스트만 출력

#all_ul = soup.find_all("ul") # 리스트형태로 반환환
#print(all_ul)

#all_ul = soup.find_all("ul") # 리스트형태로 반환환
#print(all_ul[1].text)

#class_ul =

#<div id="content"><u1 class="industry"><li>인공지능</li><li>빅데이터</li><li>스마트팩토리</li> 이 파트 가져오기 
#class industry를 가져오는 selector
# ul. industry
# #content > .industry
# #content .industry
# #content:first-child
# .industry
first_ul = soup.select_one("ul.industry")
print(first_ul.text)

all_ul = soup.select('#content > t')
