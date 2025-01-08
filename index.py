'''
def nu_ss1(numbe1, numbe2):
numbe1 = int(input(" : "))
numbe2 = int(input("매개변수를 입력하시오 : "))

if numbe1 == numbe2:
    return(f"{numbe1} * {numbe2}")
else:
    return(f"{numbe1} + {numbe2}")


'''
'''
def nu_ss1(numbe1, numbe2):

    
    if numbe1 == numbe2:
        return f"{numbe1 * numbe2}" 
    else:
        return f"{numbe1 + numbe2}"
numbe1 = int(input("매개변수를 입력하시오: "))
numbe2 = int(input("매개변수를 입력하시오: "))    
print(nu_ss1(numbe1, numbe2))

'''

def sh(it, cost):
    print(it)
    print(cost)
    if cost <= 20000:
        print("코스트가 20000 미만")
        return cost + 2500
    else:
        print("코스트가 20000이상")
        return cost

it = input("상품 입력해주세요 : ")
cost = int(input("가격을을 입력하시오 : ")) 
cost = sh(it, cost) # this is changed
print(f"{it} 가격 : {cost}원" )
