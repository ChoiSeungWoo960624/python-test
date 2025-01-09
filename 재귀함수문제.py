
def hanoi(n):
    if n <= 0: # 바닥조건
        return n
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
      return hanoi(n - 1) + hanoi(n - 2)

print(hanoi(7))
print(hanoi(6))
print(hanoi(5))
print(hanoi(4))
print(hanoi(3))