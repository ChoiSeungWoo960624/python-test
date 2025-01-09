#람다식

from re import S
from tkinter import NS


def add(x, y): # 일반 함수
    return x + y

print(add(3, 4)) # 7

add2 = lambda x,y: x + y
print(add2(4, 5)) # 9

# 매개변수가 1개인 람다식
square = lambda x: x**2
print(square(5)) # 25
print((lambda x: x**2)(5)) #25

#매개변수가 2개인 람다식
mul = lambda x, y: x * y
print(mul(3, 7))
print((lambda x, y: x * y)(3,7))

# 람다 함수를 매개변수로 전달

# call(): 함수를 인수로 받아서 그 함수를 10번 호출하는 함수
def call(func):
    for _ in range(10):
        func() # 전달받은 함수를 호출

# hello(): 일반 함수로 "안녕" 문자 출력
def hello():
    print("안녕")

# 람다식으로 정의된 함수 hello2
hello2 = lambda: print("하이")

call(hello) # call 함수엥 hello 함수를 전달해서 10번 실행
call(hello2) # call 함수에 hello2 람다식을 전달해서 10번 실행

# 고차함수 (map, filter 등) 와 함께 쓰는 람다식
# 참고. 고차함수?
# : 함수를 인수로 받을 수 있고, 함수를 반환할수도 있음

# 1. 람다식 with map()

def square(x):
    return x**3

unmbers = [2, 4, 6, 8, 10]

print(list(map(square, unmbers))) # 일반함수

print(list(map(lambda x: x**3, unmbers))) # 람다식

# 2. 람다식 with filter()
def even_number(x):
    return x % 2 == 0


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(even_number, numbers2)))  # 일반함수
print(list(filter(lambda x: x % 2 == 0, numbers2)))  # 람다식

# 3. map, fillter 두 개를 람다식과 함께 사용
# 3-1. 짝수만 남겨서 -> filter
#filter(almbda x: x % 2 == 0, numbers2)
# 3-2 그 제곱을 계산 -> map

even_squared_nums = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers2)))
print(even_squared_nums)


weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0],
]

NS_type = int(input("[날씨 데이터 분석 프로그램] \n1. 평균 기온 계산\n2. 최고|최저 기온 찾기\n3. 강수량 분석\n4. 날씨 데이터 추가\n5. 전체 데이터 출력\n6.종료\n원하는 기능의 번호를 입력하세요 : "))

if NS_type == 1:
    ot_city = input("도시 이름을 입력하세요 : ")
    if ot_city in ["서울", "부산"]:
        city_temps = [entry[2] for entry in weather_data if entry[1] == ot_city]
        if city_temps:
            avg_temp = sum(city_temps) / len(city_temps)
            print(f"{ot_city}의 평균 기온 : {avg_temp:.2f}℃")
        else:
            print ("현재 서울과 부산만 검색 할 수 있습니다.")
    else:
        print("현재 서울과 부산만 검색 할 수 있습니다.")

# elif NS_type == 2:
#     ot_city = input("도시 이름을 입력하세요 : ")
#     if ot_city in ["서울", "부산"]:
#         city_potential = [entry[2] for entry in weather_data if entry[1] == ot_city]
#         if city_potential:
            





# elif NS_type == 3:
#     pass
# elif NS_type == 4:
#     pass
# elif NS_type == 5:
#     def weather_data (day, ct, zr) :
#         ["2024-11-20", "서울", 15.2, 0.0],
#         ["2024-11-20", "부산", 18.4, 0.0],
#         ["2024-11-21", "서울", 10.5, 2.3],
#         ["2024-11-21", "부산", 14.6, 1.2],
#         ["2024-11-22", "서울", 8.3, 0.0],
#         ["2024-11-22", "부산", 12.0, 0.0],
#     print ("날짜 : {} 도시 : {} , 평균 기온 : {} , 강수량 : {}")
# elif NS_type == 6:
#     pass
    




























# vending_machine = ['게토레이', '게토레이', '레스비', '레스비', '생수', '생수', '생수', '이프로']

# try:
#     use_type = int(input("사용 종류를 입력해주세요 (1. 소비자, 2. 주인): "))

#     if use_type == 1:
#         gast_pick = input("마시고 싶은 음료를 입력하세요: ")
#         if gast_pick in vending_machine:
#             vending_machine.remove(gast_pick)
#             print(f"{gast_pick} 드릴게요.")
#         else:
#             print("현재 해당 물품은 재고가 다 떨어졌거나 없는 제품입니다.")
#         print(f"남은 음료는 {vending_machine}")

#     elif use_type == 2: 
#         host = (input("할 일 선택 : 1. 추가 2. 삭제 "))
#         if host == '추가':
#             new_it = input("추가할 음료 이름을 입력하세요: ")
#             vending_machine.append(new_it)
#             gr_it = {item: vending_machine.count(item) for item in set(vending_machine)}
#             gr_di = [f"{item}({count})" for item, count in gr_it.items()]
#             print(f"{new_it} 추가되었습니다. 현재 재고: {', '.join(gr_di)}")
        
#         elif host == '삭제':
#             del_it = input("삭제할 음료 이름을 입력하세요: ")
#             if del_it in vending_machine:
#                 vending_machine.remove(del_it)
#                 print(f"{del_it} 삭제되었습니다. 현재 재고: {vending_machine}")
#             else:
#                 print("삭제하려는 음료가 존재하지 않습니다.")
#         else:
#             print("잘못 선택하셨습니다.")
#     else:
#         print("잘못 입력하셨습니다. 다시 확인해주세요.")
# except ValueError:
#     print("잘못 입력하셨습니다. 숫자로 입력해주세요.")
