# selenium
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# # driver = webdriver.Chrome()
# # driver.get("https://naver.com")
# # input("대기")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# driver.get("https://naver.com")

# input("")

# 여기까지 webdriver 설정
# ---------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # By사용
from selenium.webdriver.common.keys import Keys  # Key사용
import time

service = Service()
driver = webdriver.Chrome(service=service)


# 브라우저 제어
# driver.get("https://google.com")
# print(driver.title)
# print(driver.current_url)
# driver.maximize_window()
# time.sleep(2)
# driver.get("https://www.wikipedia.org")
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(2)
# driver.quit()
# input("")