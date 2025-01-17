# 웹 상호작용
# driver.get("https://google.com")
# time.sleep(2)
# search_input = driver.find_element(By.NAME, "q")
# time.sleep(2)
# search_input.send_keys("selenium1")
# time.sleep(2)
# search_input.send_keys(Keys.BACKSPACE)
# # search_input.send_keys(Keys.ENTER)
# input("")

#####################################
# 스크롤과 창옵션
# driver.get("https://naver.com")
# time.sleep(2)
# driver.execute_script("alert('hello, selenium')")
# time.sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# time.sleep(2)
# alert.accept()  # 확인버튼 클릭

# # element창찾기
# search_input = driver.find_element(By.XPATH, '//*[@id="query"]')
# search_input.send_keys("selenium")
# search_input.send_keys(Keys.ENTER)
# input("")

##############################################
# # 무한스크롤
# driver.get("https://www.google.com/imghp?hl=ko&ogbl")
# search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
# search_input.send_keys("토끼")
# search_input.send_keys(Keys.ENTER)

# for i in range(3):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)


# input("")