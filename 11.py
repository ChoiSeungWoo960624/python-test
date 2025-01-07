#리스트 내포
# : 파이썬에서 리스트를 간결하게 생성하는 문법


numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares) #[1, 4, 9, 16, 25]

squares2 = [n**2 for n in range(1, 6)]
print(squares2) #[1, 4, 9, 16, 25]

# 조건문과 함께 사용
even_squares = [x**3 for x in range(1, 6) if x % 2 == 0]
print