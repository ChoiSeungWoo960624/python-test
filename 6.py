# 튜플, tuple
t1 = (1,)  # 요소가 1개인 튜플은 반드시 쉼표 사용!
print(t1)  # (1,)

not_tuple = (1)
print(not_tuple)  # 1 <- 정수

t2 = (1, 2, 3, 4, 5, 3, 3, 4, 3)  # 괄호를 사용해 튜플 선언
print(t2)  # (1, 2, 3, 4, 5, 3, 3, 4, 3)

t3 = 1, 2, 3  # 괄호 없이 쉼표만 사용 튜플 선언 가능
print(t3)  # (1, 2, 3)

t4 = ("a", "b", "c", ("안녕", "감자"))  # 튜플 안에 중첩 튜플
print(t4)  # ('a', 'b', 'c', ('안녕', '감자'))

# 튜플의 요소 접근 및 메서드 사용
print(t1[0])  # 1
print(t2.count(3))  # 4 <- 3의 개수
print(t3.index(2))  # 1 <- 2의 위치
print(t4[3][0]) # 안녕
print(t4[:2]) # ('a', 'b')

print("a" in t4) #사실
print("b" in t4) #사실

#t4[0] = "x"
# TypeError: 'tuple' object does not support item assignment