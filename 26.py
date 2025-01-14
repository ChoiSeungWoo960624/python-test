# 모듈 불러오기 : 확장자를 생략하여 파일명으로 불러옴
import calculator

# 모듈의 함수 사용
print(calculator.add(5, 7)) # 12
print(calculator.sub(5, 7)) # -2
print(calculator.divide(5, 1)) # 
print(calculator.divide(10, 3)) #


#모듈의 변수 사용
print(calculator.PI) #3.141592
print(calculator.e)

# 모듈의 클래스 사용
calc1 = calculator.Calculator()
print(calc1.multiply(4, 3)) #12
print(calc1.square(4))

import calc
import calc as a #별칭 calc 대신 a로 이름변경하여 사용

import calc as a 
#모듈명.함수명
print(a.add(5, 2))
print(a.sub(5, 2))
print(a.multiply(5, 2))
print(a.divide(5, 2))
