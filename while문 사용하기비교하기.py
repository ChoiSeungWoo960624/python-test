'''
age = int(input("나이를 숫자로 입력해주세요 : "))
method = input("결제방법을 입력해주세요 (현금 또는 카드) : ")
pay = (pay1, pay2, pay3, pay4, pay5, pay6)
pay1 = "무료"
pay2 = "450원"
pay3 = "720원"
pay4 = "1000원"
pay5 = "1200원"
pay6 = "1300원원"

if age >= 0 and age <= 200:
    if age < 7:
        print(f"{pay1} 입니다.")
elif age < 13:
        print("{pay2} 입니다.")
elif age < 19:
    if pay == "현금":
        print("{pay3} 입니다.")
    elif pay == "카드":
        print("{pay4} 입니다.")
elif age_pa < 74:
    if pay == "현금":
        print("{pay5}} 입니다.")
elif pay == "카드":
        print("{pay6} 입니다.")
elif age < 75:
    print("{pay1} 입니다.")

print(f"{age}세의 요금은 {pay}입니다.")
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
        pay = "요금 계산 불가"
else:
    pay = "올바른 나이를 입력해주세요."

print(f"{age}세의 요금은 {pay}입니다.")