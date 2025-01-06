"""
#리스트
number = [1, 2, 3, "Hello", "Python"]
print (number)

# 인덱싱 (indexing) : 인덱스 번호로 요소를 추출하는 행위
print (number[3]) #number안에 인덱스 3번째꺼 출력.
print (number[0]) #number안에 인덱스 0번째꺼 출력.
#print (number[10]) #number안에 인덱스 10번째꺼 출력. - 범위가 넘어갈 때는 오류 발생. 

# list() 함수 : 리스트를 생성하는 내장함수 (반복 가능한 객체를 리스트로 변환할 때 사용)
# 반복 가능한 객체? (ex. 문자열, 튜플, 셋(집합), 딕셔너리, 또 다른 리스트)
text = "Hello, Python"
print (list(text)) #['H', 'e', 'l', 'l', 'o', ',', ' ', 'P', 'y', 't', 'h', 'o', 'n'] 공백도 리스트화함.

#invalid = 1234
#print (list(invalid)) # TypeError: 'int' object is not iterable(반복가능한) [정수는 반복 가능한 객체가 아님]

# ex)문자열의 인덱싱과 슬라이싱 
text = "Hello, Python"
print (text[7]) # P
print (text[7] + text[8] + text[9] + text[10] + text[11] + text[12]) #Python
print (text[7:])

# 퀴즈. 문자열 슬라이싱
date = "20250106"
year = date[0:4]
month = date[4:6]
day = date[6:]
print (year + "년" + month +"월" + day + "일") # 2025년 01월 06일

#문자열에서 사용 가능한 함수
print (len(date)) # 8 #len() : 문자열의 길이를 구하는 함수
print (len(text)) # 13 
print (text.count("l")) # 2  #count() : 문자열의 길이를 구하는 함수
print (text.count("P")) # 1
print (text.count("p")) # 0 # 대소문자 구별 가능
print (text.count("J")) # 0 없는건 0이라고 뜬다.

#리스트 인덱싱과 슬라이싱
shop = ["반팔", "청바지", "이어폰", ["무선키보드", "기계식키보드"]]
print (shop[:2]) # 0, 1 ['반팔', '청바지'] 0 <= shop < 2
print (shop[3]) #['무선키보드', '기계식키보드']
print (shop[-2]) # 이어폰
print (shop[:]) #['반팔', '청바지', '이어폰', ['무선키보드', '기계식키보드']]

# 리스트 수정
#shop [0] = "긴팔"
#print (shop) #['긴팔', '청바지', '이어폰', ['무선키보드', '기계식키보드']]
#shop [100] = "신발"
#print (shop) # IndexError: list assignment index out of range 존재할 수 있는 범위내에서 바꿀 수 있다.

#리스트 삭제
del shop [1] # 단일 삭제
print (shop) #['반팔', '이어폰', ['무선키보드', '기계식키보드']]

del shop[2:] # 복수 삭제
print (shop) # ['반팔', '이어폰']

# 리스트 연산
a = [1, 2, 3]
b = ["안녕", "반가워"]
print (a + b) # [1, 2, 3, '안녕', '반가워'] #이어쓰기
print ( b * 3) # ['안녕', '반가워', '안녕', '반가워', '안녕', '반가워'] #반복하기
"""

# 정렬 함수
# asc : ascending 오름 차순
# desc : desceding 내림 차순
num = [3, 1, 5, 2]
num_asc = sorted(num)
print (num) # [3, 1, 5, 2]
print (num_asc) # [1, 2, 3, 5]

num_desc = sorted(num, reverse = True)
print (num_desc) # [5, 3, 2, 1]

num.sort() # 원본이 변경되는 메서드
print (num ) # [1, 2, 3, 5]

# 문자 정렬
korean = ["강", "김", "최", "이", "한"]
korean.sort(reverse=True)
print (korean) #['한', '최', '이', '김', '강']

alphabet = ["b", "c", "a", "d"]
alphabet.reverse() #내림차순이 아니라 인덱스 역순 
#-> 새로운 리스트 반환하지 않고 원본 리스트를 변경
print (alphabet) #['d', 'a', 'c', 'b']
print (alphabet.index("c")) # 2

a = ["a", "b", "c", "안녕", "hi"]
print (a) # ['a', 'b', 'c', '안녕', 'hi']

a.append("GOOD")
print(a) # ['a', 'b', 'c', '안녕', 'hi', 'GOOD']

a.pop()
print(a) #['a', 'b', 'c', '안녕', 'hi']

a.pop(2)
print(a) #['a', 'b', '안녕', 'hi']

a.remove("안녕")
print(a) # ['a', 'b', 'hi']

a.insert(2, "잘가")
print(a) #['a', 'b', '잘가', 'hi']

a.clear()
print(a) # []

x = ["q", "w", "d", "r", "m"]
print(x.count("w")) # 1

#연습문제-실습.리스트 연습문제
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print (rainbow[1:3]) # 1. 1~2번 인덱스 값 출력
rainbow_asc = sorted(rainbow)
print (rainbow_asc) # 알파벳 순서로 정렬한 값 출력
rainbow.append("nave")
print (rainbow) # 좋아하는 색 맨 마지막에 추가하기
del rainbow[3:7]
print (rainbow) # 3~6번째 값 삭제하기