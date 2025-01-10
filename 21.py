''''
#캡슣화 
#정보 음닉
class Person:
    def __init__(self):
        # 멤버변수 (_name, _age) 언더스코어?
        #-> protected 접근제어로 간주
        #-> 외부에서 직접 접근하지 않고, 해당/서브 클래스에서 사용
        # "직접 접근"대신 -> getter/setter를 이용해서 값을 읽거나 / 수정하도록 함 -> 데이터 보호호
        self._name = ""
        self._age = 0

    def setname(self, name):
        self._name = name

    def getname(self):
        return self._name
    
    def setage(self, age):
        self._age = age
    
    def getage(self):
        return self._age
    
p1 = Person()
p1.setname("농부")
p1.setage(35)
print("이름: ", p1.getname())
print("나이: ", p1.getage())

p2 = Person()
p2.setname("놀부")
p2.setage(38)
print("이름: ", p2.getname())
print("나이: ", p2.getage())
'''


class supermarket:
    pl_num = 0

    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def _location(self):
        return location

    def show_list(self):
        return product

    def _category(self,show_list):
        return show_list
        
    def enter_customer(selfm, customer):
        customer.pl_num +=  1 # 클래스 변수 값을 1 증가
        customer.pl_num = customer
        self.customer = customer
    
    def show_info(self):
        return f"위치: {location}, 이름 : {name}, 상품 : {product}, 고객 수: {customer}"


location = input("위치 : ")
name = input("가게이름 : ")
product = input("파는 물건 : ")
customer = float(input("고객의 수 : ")) 
market = (location, name, product, customer)

print(market.show_info())
