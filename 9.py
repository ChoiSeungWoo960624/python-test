# 조건문

# if 문
'''
age = 20
if age < 20: # 20 < 20 -> False
    print("미성년자 입니다.")

print(f"나이는 {age}(세) 입니다.")

age = 17

if age < 20: # 17 < 20 -> False
    print("삐비빅빅") #블럭안 에 여러가지 넣을 수 있음
    print("미성년자 입니다.")

print(f"나이는 {age}(세) 입니다.")
'''

# else문
# 조건문
"""
age = 17

# if 문

if age < 20:
    print("미성년자 입니다")

if age >= 20:
    print("성인 입니다")

print(f"나이는 {age}(세) 입니다")
"""

'''
# else 문
if age < 20:
    print("미성년자 입니다")
else:
    print("성인 입니다")
'''
'''
# elif문 == (else if)
age = input("나이를 입력하세요") #imput 문자열로 저장

if age < 20:
    print("10대입니다.")
elif age < 30:
    print("20대입니다")
elif age < 40:
    print("30대입니다")
elif age < 50:
    print("40대입니다")
else:
    print("50대 이상입니다")

'''
'''
NA = input("비밀번호를 입력하세요 : ")
NA = ("abc123")
if NA == ("abc123"):
    print("비밀번호가 맞습니다.")
else:
    print("비밀번호가 맞지않습니다.")
'''
'''
credit = int(input("점수를 입력하세요 : "))
if credit < 60:
    print("학점 :  F")
elif credit < 70:
    print("학점 :  D")
elif credit < 80:
    print("학점 :  C")
elif credit < 90:
    print("학점 :  B")
else:
    print("학점 :  A")
'''
'''
NA = int(input("비밀번호를 입력하세요 : "))
NA = ("abc123")
if NA == ("abc123"):
    print("비밀번호가 맞습니다.")
else:
    print("비밀번호가 맞지않습니다.")

ja = int(input("숫자를 입력하세요."))
if ja%2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
'''

# 불리언(Boolean) : 참과 거짓을 나타내는 데이터 타입.
# 참 : True
# 거짓 : False

'''
# 중첩 조건문.
is_login = True
roie = "admin"
if is_login:
    print("로그인 상태입니다.")
    if roie == "admin":
        print("관리자 권한을 갖습니다.")
    elif roie == "aditor":
        print("관리자 권한을 갖습니다.")
    else:
        print("일반 사용자입니다.") 
else:
    print("로그인이 필요합니다.")

# 삼항 연산자
age = 33
status = "성인" if age >= 20 else "미성년자"
print(status) # 성인인

number = 7
result = "짝수" if number % 2 == 0 else "홀수"
print(result) #홀수

a, b = 5, 7
max_value = a if a> b else b
print(max_value) # 7

# 중첩 삼항 연산자
score = 91
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
'''

'''
# 조건문에서 in 연산자 활용
users = ["sean", "Linda", "Allie", "Martin"]
username = input("Name >> ")

if username in users:
    print(f"환영합니다, {username}님!")
else:
    print("등록되지 않은 사용자입니다. 회원가입을 진행해주세요.")

'''
age = int(input("나이를 숫자로 입력해주세요 : "))
method = input("결제방법을 입력해주세요 (현금 또는 카드) : ")

pay1 = "무료"
pay2 = "450원"
pay3 = "720원"
pay4 = "1000원"
pay5 = "1200원"
pay6 = "1300원"

if 0 <= age <= 200:  # 나이 유효성 검사
    if age < 7:
        pay = pay1
    elif age < 13:
        pay = pay2
    elif age < 19:
        if method == "현금":
            pay = pay3
        elif method == "카드":
            pay = pay4
        else:
            pay = "결제 방법이 올바르지 않습니다."
    elif age < 74:
        if method == "현금":
            pay = pay5
        elif method == "카드":
            pay = pay6
        else:
            pay = "결제 방법이 올바르지 않습니다."
    elif age >= 75:
        pay = pay1
    else:
        pay = "무료"
else:
    pay = "올바른 나이를 입력해주세요."

print(f"{age}세의 요금은 {pay}입니다.")
''''''



'''
#실습 2
gs = {"apple": 95, "banana": 105, "cherry": 50}
gsname = input("과일을 영문으로 입력하세요. >> ")
if gsname in gs:
    print(f"{gsname}의 칼로리는 {gs[gsname]}Kcal입니다.")
else:
    print("입력한 과일 정보가 없습니다.")
 '''

'''
여기 복습해줘...
# while 문
i = 5
while i > 0:
    print("반복문 연습", i)
    i -= 1
print("종료")

# 합계 구하기
num = 1  # 더하는 숫자
total = 0  # 총합
while num <= 10:
    total += num  # total = total + num
    print("현재 total 값 > ", total)
    num += 1  # num = num + 1

print(f"1부터 10까지의 합은 {total}입니다.")

# 입력값 받기
user_input = ""
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. '종료' 입력시 종료됩니다.")
    print(f"입력한 값: {user_input}")

print("프로그램이 종료되었습니다.")
'''

'''
# while 문
i = 5
while i > 0:
    print("반복문 연습", i)
    i -= 1
print("종료")
"""
# 합계 구하기
num = 1  # 더하는 숫자
total = 0  # 총합
while num <= 10:
    total += num  # total = total + num
    print("현재 total 값 > ", total)
    num += 1  # num = num + 1

print(f"1부터 10까지의 합은 {total}입니다.")

# 입력값 받기
user_input = ""
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. '종료' 입력시 종료됩니다.")
    print(f"입력한 값: {user_input}")

print("프로그램이 종료되었습니다.")
"""
'''
# break 문
# 예시. 숫자를 입력받아서 0이 입력되면 반복문 종료
while True:
    num = int(input("숫자 입력(0 입력시 종료):"))

    if num == 0:
        print("프로그램 종료")
        break

    print(f"입력한 숫자는 {num}입니다")
'''

# continue 문
# 예시. 숫자 입력받고 짝수만 출력하고 홀수는 건너뛰기
while True:
    num = int(input("숫자 입력(음수 입력시 종료)"))

    if num < 0:
        print("프로그램 종료")
        break # 음수 입력시 프로그램 종료
    
    if num % 2 != 0:
        continue #홀수는 건너뛰고, 다시입력 받기
    print(f"입력한 짝수는 {num}입니다.")
'''

'''
#////////// 아예 해결 못함 while문 사용하기
NU = int(input("숫자를 입력해주세요. : "))
num = 1
total = 0
user_ch = ""
while user_ch != "종료":
    user_ch = input ('"종료"라고 입력하면 프로그램이 종료됩니다. ')
        break
    print(f"입력한 값: {user_ch}")
print("프로그램이 종료되었습니다.")

while num <= inf: #infinite 범위 정하기기
    total += NU + num
    num += 1
print(f"1부터{NU}까지의 합은{total}입니다.")

int(input("양수만 입력 하세요."))
    if NU == int:
        continue
'''''

