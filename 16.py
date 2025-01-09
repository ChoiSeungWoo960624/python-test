#내장 함수

# abs(정수) : 절댓값 구하는 내장함수
import numbers


print(abs(-77)) # 77
print(abs(0)) # 0
print(abs(10)) # 10
print(abs(-10)) # 10

# 만약에, abs() 내장함수가 없었다면?
def my_abs(n):
    if n < 0:  # 음수라면, 양수로 변환하여 반환
        return -n
    else:  # 0 혹은 양수이니 그대로 반환
        return n


print(my_abs(-77))
print(my_abs(0))
print(my_abs(10))

# pow(x, y): x^y 구하는 내장함수
print(pow(10, 2))
print(pow(2, 10))
print(pow(3, 4))

# 만약에, abs() 내장함수가 없었다면?
def my_pow(x, y): # x: 밑, y: 지수
    num = 1 #초기값

    for i in range(0, y):
        unm *= i
    return num


def my_pow(x, y): # x: 밑, y: 지수
    num = 1 #초기값

    for _ in range(0, y):
        unm *= x
    return num

print(pow(10, 2))
print(pow(2, 10))
print(pow(3, 4))

# map()

# 각 요소마다 적용하고 싶은 함수 square
def square(x):
    return x**3

# 리스트
unmbers = [2, 4, 6, 8, 10]

print(map(square, unmbers)) # <map object at 0x000002D932FE7670>
print(list(map(square, unmbers))) # [8, 64, 216, 512, 1000]

# filter()
def even_number(x):
    return x % 2 == 0

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter(even_number, numbers2)) #<filter object at 0x000001C0B07E6DD0>
print(list(filter(even_number, numbers2))) #[2, 4, 6, 8, 10]



nu1 = int(input("1부터 30까지 앞 배수 설정"))
nu2 = int(input("1부터 30까지 뒷 배수 설정"))

if 1 <= nu1 <= 30:
    def bs(nu) :
        if nu1 >= nu2:
            def ss(a):
                [nu1 % nu2 == 0]
                print(f"{nu1}의 배수는 {ss(a)}")
        else:
            print("입력값이 올바르지 않습니다.")
else:
    print("값이 올바르지 않습니다.")    



    