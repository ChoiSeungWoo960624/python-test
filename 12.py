'''
# 이중 for 문
for i in range(5):
    print(f'외부 반복문의 i 값 : {i}')

    for j in range(3):
        print(f"내부 반복문의 j 값 : {j}")

    print("-------------------")

외부 반복문의 i 값 : 0
내부 반복문의 j 값 : 0
내부 반복문의 j 값 : 1
내부 반복문의 j 값 : 2
-------------------
외부 반복문의 i 값 : 1
내부 반복문의 j 값 : 0
내부 반복문의 j 값 : 1
내부 반복문의 j 값 : 2
-------------------
외부 반복문의 i 값 : 2
내부 반복문의 j 값 : 0
내부 반복문의 j 값 : 1
내부 반복문의 j 값 : 2
-------------------
외부 반복문의 i 값 : 3
내부 반복문의 j 값 : 0
내부 반복문의 j 값 : 1
내부 반복문의 j 값 : 2
-------------------
외부 반복문의 i 값 : 4
-------------------
-------------------
외부 반복문의 i 값 : 4
내부 반복문의 j 값 : 0
내부 반복문의 j 값 : 1
-------------------
외부 반복문의 i 값 : 4
내부 반복문의 j 값 : 0
-------------------
외부 반복문의 i 값 : 4
-------------------
외부 반복문의 i 값 : 4
내부 반복문의 j 값 : 0
내부 반복문의 j 값 : 1
내부 반복문의 j 값 : 2
-------------------
'''

# 이차원 리스트와 이중 for 문
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 ,9]
]
for row in matrix:
    print(f"외부반복문의 row: {row}")
    #외부반복문의 row: [1, 2, 3]
    #외부반복문의 row: [4, 5, 6]
    #외부반복문의 row: [7, 8, 9]
    
    for elem in row:

        print(f"외부반복문의 elem: {elem}") #단어 블럭잡고 ctrl + d 누르면 현재 블럭 잡힌 같은 단어를 수정할 수 있게 해준다.

'''
외부반복문의 row: [1, 2, 3]
외부반복문의 elem: 1
외부반복문의 elem: 2
외부반복문의 elem: 3
외부반복문의 row: [4, 5, 6]
외부반복문의 elem: 4
외부반복문의 elem: 5
외부반복문의 elem: 6
외부반복문의 row: [7, 8, 9]
외부반복문의 elem: 7
외부반복문의 elem: 8
외부반복문의 elem: 9
'''

'''
# 요소(elem 변수)의 합계 구하기
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 ,9]
]
total_sum = 0
for row in matrix:
    # print(f"외부반복문의 row: {row}")
    for elem in row:
        # print(f"내부반복문의 elem: {elem}")
        total_sum += elem
    # 1번 시점: 내부 반복문이 종료될 때
    # print(f"중간 합계: {total_sum}")
# 2번 시점: 외부 반복문이 종료될 때
print(f"전체 합계: {total_sum}")
#전체 합계: 45
'''

'''
# 짝수만 출력하기
matrix = [
    [21, 22, 33],
    [44, 25, 62],
    [17, 18 ,91]
]
print("짝수만 출력:", end=" ")
for row in matrix2:
    for elem in row:
        if elem % 2 == 0: # 조건문
            print(elem, end=" ")
'''


for i in range(2,10):
    for j in range(1,10):
        print(f'{i} x {j} ={i*j}')
    print("-------------------")