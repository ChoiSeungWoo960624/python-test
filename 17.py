#재귀 함수

def sos(i):
    print(f"{i}번째 도움 요청")

    if i == 1:
        return ""
    else:
        return sos(i - 1)

sos(10)

# ex. 팩토리얼

def factorial(n):
    print("n >>", n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(3))
print(factorial(5))
print(factorial(7))