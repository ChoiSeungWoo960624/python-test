# 실습. 로또 번호 뽑기

import random

#1.
lotto = sorted(random.sample(range(1, 46), 6))
print(lotto)

poto_lot = float[1, 46]
rand_sample = random.sample(poto_lot, 6)
print(f"sample: {rand_sample}")

#2.
#1. 빈 set 만들기
lotto_nums = set()

# 2. 6번 숫자 뽑기
while len(lotto_nums) < 6:
    #난수를 set 에 추가
    lotto_nums.add(random.randint(1, 45)) # randint b값을 포함함

# 3. 오름차순 정렬
sorted_lotto_nums = sorted(lotto_nums)
print(sorted_lotto_nums)

