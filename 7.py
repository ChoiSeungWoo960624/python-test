# 셋 (set)

s1 = {1, 2, 3, 3, 4} # 중복 허용 x
print(s1) # {1, 2, 3, 4}

s1.add(5) # 원소 추가
print(s1) # {1, 2, 3, 4, 5}

#update()
# 다른 set, list, tuple의 요소들을 현재 집합에 추가하는 기능
s1.update([6, 7, 8, 9, 8, 10]) 
print(s1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s1.remove(3)
print(s1) # {1, 2, 4, 5, 6, 7, 8, 9, 10}

#s1.remove(100) # KeyError: 100 # 존재하는 요소만 삭제 가능

s1.discard(9) # 요소 삭제
s1.discard(100) # 존재하지 않는 요소 삭제해도 오류 발생 x
print(s1) # {1, 2, 4, 5, 6, 7, 8, 10}

s1.clear()
print(s1) # set() <- 빈 집합

# set 연산
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

#합집합
s3 = s1.union(s2)
#s3 = s1 | s2 # 혹은 이 코드 {1, 2, 3, 4, 5, 6, 7, 8}
print(s3) # {1, 2, 3, 4, 5, 6, 7, 8}

#교집합
s3 = s1.intersection(s2)
#s3 = s1 & s2
print(s3) #{4, 5}

#차집합
# s3 = s1.difference(s2)
# s3 = s1 - s2

# s3 = s2.difference(s1)
s3 = s2 - s1
print(s3) #{8, 6, 7}

# in 키워드
print(1 in s1) # true
print(100 in s1) #false

# len()
print(len(s1)) # 5