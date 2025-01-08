'''
#전역 변수
quantity = 10

def get_price(price):
    #price : 매개 변수
    return price * quantity

print(f"{quantity} 개의 가격은 {get_price(5000)}입니다.")
#10 개의 가격은 50000입니다.

#지역 변수
def oneUp():
    x = 0
    x += 1
    return x

print(oneUp())
#print(x) #NameError: name 'x' is not defined x가 지역이라 메모리가 사라져 정의되지않음
print(quantity)


# 변수의 유효 범위
amount = 10
def price_sum(price):
    return price * amount
print(price_sum(2000)) #20000


amount = 10
def price_sum(price):
    amount = 7
    return price * amount
print(price_sum(2000)) #14000

# global 키워드
x = 0
def onuUP():
    global x # 함수 내에서 전역변수 "변경"이 이루어질 예정정 힌트
    x += 1
    return x

print(onuUP())
print(onuUP())
print(onuUP())

x = 0
def onuUP():
    #global x # 함수 내에서 전역변수 "변경"이 이루어질 예정정 힌트
    x += 1       #색 주목 x의 위 x랑 다르게 인식됨
    return x     #색 주목 x의 위 x랑 다르게 인식됨됨

print(onuUP())
print(onuUP())
print(onuUP())
'''

