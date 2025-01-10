#클래스 
''''
# 클래스 정의
class Car:
    # 2개의 속성을 가짐
    model = ""
    cc = 0

car1 = Car() #인스턴스 생성
car1.model = "bmw"
car1.cc = 4000

car2 = Car() #인스턴스 생성
car2.model = "페라리"
car2.cc = 40000


print(f"모델명: {car1.model}")
print(f"베기량: {car1.cc}")

print(f"모델명: {car2.model}")
print(f"베기량: {car2.cc}")

# 클래스 정의
class Car:
    # 2개의 속성을 가짐
    model = ""
    cc = 0

    # 매서드 추가
    def info(self):
        print(f"모델명 : {self.model}, 배기량: {self.cc}cc")

car1 = Car() #인스턴스 생성
car1.model = "bmw"
car1.cc = 4000

car2 = Car() #인스턴스 생성
car2.model = "페라리"
car2.cc = 40000

car1.info()
car2.info()

from mimetypes import init


class car:
""" 
 def __init__(self, 매개변수 1, 매개변수2 , ....):
     self.속성1 = 매개변수1
     self.속성2 = 매개변수2
     ....
     # 생성자의 매개변수와 값으로 객체의 속성을 초기화(할당) 
 """

 # 생성자자
 def __init__(self, model, cc):
     self.model = model
     self.cc = cc

 def info(self):
        print(f"모델명 : {self.model}, 배기량: {self.cc}cc")

#인스턴스_생성
car1 = car("bmw", 2200)
car2 = car("페라리", 40000)
car1.info()
car2.info()
print(car1)
print(car2)

 # 생성자자
def __init__(self, model, cc):
     self.model = model
     self.cc = cc

def __init__(self):
        return(f"모델명 : {self.model}, 배기량: {self.cc}cc")

def info(self): #매서드를 보여 주기 위한 것것
        print(f"모델명 : {self.model}, 배기량: {self.cc}cc")

#인스턴스_생성
car1 = car("bmw", 2200)
car2 = car("페라리", 40000)
car1.info()
car2.info()
print(car1)
print(car2)
'''

'''
print("=====승용차 리스트=====")
cars = [car("소나타, 2000"), car("쏘랜토", 4000), car("아반떼", 1600)]

"""
snt = Car("소나타", 2000)
srt = Car("쏘렌토", 3000)
avt = Car("아반떼", 1600)
cars2 = [snt, srt, avt]
"""

for car in cars:
    print(car)
    # car.info()
'''





''''
maso1 = int(input("숫자"))
maso2 = int(input("숫자"))
class calculator:
    def __init__(self, masol, maso2):
    self.add(Self) = mao1 + maso2
    self.sub(Self) = mao1 - maso2
    self.mul(Self) = mao1 * maso2
    self.div(Self) = mao1 / maso2

Calculator(10, 7)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())
'''
class calculator:
    def __init__(self, masol, maso2):
        self.maso1 = masol
        self.maso2 = maso2
    
    def add(Self):
        return maso1 + maso2
    
    def sub(Self):
        return maso1 - maso2
    
    def mul(Self):
        return maso1 * maso2
    
    def div(Self):
        if maso1 / maso2 != 0:
            return maso1 / maso2
        
maso1 = int(input("앞자리_숫자 : "))
maso2 = int(input("뒷자리_숫자 : "))


calc = calculator(maso1, maso2)

print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())


class calculator:
    def __init__(self, masol, maso2):
        self.maso1 = masol
        self.maso2 = maso2
    
    def add(Self):
        return maso1 + maso2
    
    def sub(Self):
        return maso1 - maso2
    
    def mul(Self):
        return maso1 * maso2
    
    def div(Self):
        if maso2 == 0:
         return "0으로 나눌 수 없습니다."
        
        elif    maso1 / maso2 != 0:
            return maso1 / maso2
        
        return maso1 / maso2 #arly return 
#arly return
#: 조건을 먼저 체크하고, 조건이 만족되면 즉시 값을 반환하여 더이상 코드가 실행되지 않도록 하는 기법


maso1 = int(input("앞자리_숫자 : "))
maso2 = int(input("뒷자리_숫자 : "))


calc = calculator(maso1, maso2)

print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())
