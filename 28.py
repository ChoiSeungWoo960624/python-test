'''
import math

print(math.pi) # 파이값 출력
print(math.sqrt(25)) # 제곱근
print(math.factorial(4)) # 팩토리얼

print(math.ceil(3.14)) # 올림
print(math.floor(3.14)) # 내림
print(round(3.14)) # 반올림 3
print(round(3.74)) # 반올림 4
#참고. round() 함수는 math 모듈에 속한 함수가 아닌
# 파이썬 내장 함수
'''

from pickletools import long1
import math, random

rand_int = random.randint(1, 10) # a, b 모두 포함하여 임의의 정수 리턴
print(f"randint: {rand_int}")

rand_float = random.uniform(1.5, 6.5)
print(f"uniform: {rand_float}") # a, b 모두 포함하여 임의의 실수 리턴

rand_between = random.random() # 0 <= x < 1 사이의 임의의 실수 리턴 ( 1 미포함함)
print(f"uniform: {rand_between}")

# a <= x < b 사이의 정수 리턴 (b 미포함)
rand_rang = random.randrange(10, 1000)
print(f"randrange: {rand_rang}")

# 리스트에서 무작위로 하나 선택
nums = [1, 2, 3, 4, 5, 6, 7]
rand_choice = random.choice(nums)
print(f"choice: {rand_choice}")

#sample(population, k)
#- population : 모집단 (리스트, 튜플, 문자열, range())
# - k: 선택할 요소 개수
# : population에서 k 만큼 무작위 추출 (k 값은 population 크기보다 클 수 없음)
# 참고. https://docs.python.org/ko/3/library/random.html#random.sample
# 중복허용
fruits = ["사과", "포도", "거봉", "바나나", "황금향"]
rand_sample = random.sample(fruits, 2)
print(f"sample: {rand_sample}")




