from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # By사용
from selenium.webdriver.common.keys import Keys  # Key사용
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#옵션객체 생성
chrome_optin = Optinos()
#옵션 추가가
chome_o

# """
# EC메서드(대기조건)
# EC.title_is(문자열) : 현재페이지 제목이 지정된 문자열과 일치할때
# EC.title_contains(문자열) : 현재페이지 제목에 문자열이 포함될때
# EC.presence_of_element_located((By.ID, "아이디값"))  #DOM이 존재할때(화면에표시안되도됨)
# EC.visibility_of_element_located((By.CSS_SELECTOR, "선택자")) #DOM이 존재할때(화면에표시)
# EC.presence_of_all_elements_located((By.CSS_SELECTOR, "선택자")) #DOM에 모든요소가 존재할때
# EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "선택자")) #DOM에 모든요소가 존재할때
# EC.element_to_be_clickable((By.CSS_SELECTOR, "선택자")) # 요소가 화면에 표시되고 클릭이 가능할때
# EC.element_to_be_selected((By.CSS_SELECTOR, "선택자")) # 요소가 선택된 상태가 될때
# """

# # 검색입력 필드대기
# search_input = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "q"))
# )
# search_input.send_keys("python")
# search_input.send_keys(Keys.ENTER)

# input("")

# search_input = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "q"))
# )

# email_text = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
# href = email_text.get_attribute("href")
# print(href)

# input("")

####################################
#스크린샷
# driver.get("https://www.youtube.com/")
# time.sleep(2)
# driver.save_screenshot("youtube.png")

# input("")

# #스크린샷
# driver.get("https://www.youtube.com/")
# time.sleep(2)
# driver.save_screenshot("youtube.png")

# input("")


#=================================
driver.get("https://www.nate.com/")
time.sleep(2)
search_input = driver.find_element(By.XPATH, '//*[@id="q"]')
search_input.send_keys("파이썬")
search_input.send_keys(Keys.ENTER)
time.sleep(2)
driver.save_screenshot("python.png")