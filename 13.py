#함수
# 1. 매개변수x, 리턴값 x
#함수 정의
import re


def say_hello():
    print("Hello, word")

say_hello() #함수 호출출 
#Hello, word

# 2. 매개변수o, 리턴값x
# 2-1. 매개변수 1개
def print_greeting(name): #함수 정의
    print(f"Hello, {name}")

print_greeting("allie") #함수 호출 
#Hello, allie
print_greeting("martin") #함수 호출
#Hello, martin

# 2-2. 매개변수 2개
def gugudan(dan, end):
    print(f"{dan}단")
    for i in range(1, end): # 1 ~ end-1
        print(f"{dan} x {i} = {dan * i}")

gugudan(7, 15)
'''
7단
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
7 x 11 = 77
7 x 12 = 84
7 x 13 = 91
7 x 14 = 98
'''
gugudan(4, 20)
'''
4단
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
4 x 11 = 44
4 x 12 = 48
4 x 13 = 52
4 x 14 = 56
4 x 15 = 60
4 x 16 = 64
4 x 17 = 68
4 x 18 = 72
4 x 19 = 76
'''

#3. 매개변수x, 리턴값o
def mul_numbers(): # 함수 정의
    print("곱셈을 시작합니다.")
    return 10 * 5

result = mul_numbers() # 함수 호출
print(result)
#곱셈을 시작합니다.
#50


#4. 매개변수o, 리턴 값 o
def add_numbers(x, y):
    print("덧셈을 시작합니다")
    return x + y


result2 = add_numbers(40, 50)
print(result2)
print(add_numbers(40, 30))
print(add_numbers(10, 30))

# 다양한 타입을 return 하는 함수
# 1. List 타입을 반환하는 함수
#ex. 제한값(limit) 미만의 짝수를 출력하는 함수
def print_even_numbers(limit):
    return [i for i in range(0, limit) if 1 % 2 == 0]

print(print_even_numbers(10))

# 2. Dictionary 타입을 반환하는 함수
def print_user_info(name, grade):
    return {"user_name": name, "user_grade": grade}

print(print_user_info("allie", 2))
print(print_user_info("bob", 4))

# 3. set 타입을 반환하는 함수
#print(set("Hello")) # {'l', 'o', 'e', 'H'}
# 문자열을 set 타입으로 변환 => 고유한 문자들만 남긴다.
def print_unique_char(word):
    return set(word)

print(print_unique_char("Hi, my name is sean"))

# 4. Tuple 타입을 반환하는 함수
# ex. 두 숫자의 합과 곱을 동시 반환 => (합, 곱)
def calculate_sum_and_product(a, b):
    return (a + b, a * b)


print(calculate_sum_and_product(3, 5))
print(calculate_sum_and_product(7, 8))


# Collection (컬렉션)
# 혼합 컬렉션
# ex. 딕셔너리 안에 리스트가 있는 예시
def split_numbers(numbers):
    even_nums = [n for n in numbers if n % 2 == 0]  # 리스트
    odd_nums = [n for n in numbers if n % 2 != 0]  # 리스트

    # 반환값 (딕셔너리)
    return {"odd": odd_nums, "even": even_nums}


print(split_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



# 매개변수로 리스트를 받는 함수
# ex. 각 요소를 2배로 만드는 함수
def double(nums):
    return [i * 2 for i in nums]

print(double([1, 2, 3, 4]))

# ex. 각 요소를 문자열로 변환하는 함수
def to_string(nums):
    return [str(i) for i in nums]


print(to_string([8, 16, 24]))


