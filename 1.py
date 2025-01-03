# 한 줄 주석
'''
여기는
여러줄
주석입니다.
'''

"""
쌍따옴표 세 개도
여러줄
주석입니다.
"""

# 주석 처리 예시 (Ctrl + / 사용 가능)

# print ("hello world")
# print ("hello", "world")
# print ("hello")
# print ("hello", "word", sep="")  # sep: 구분자
# print ("010", "8280", "0745", sep="-")
# print ("hello", "python", 1, 2, sep="_")  # 자료형이 달라도 가능
# print ()  # print 함수 안에 아무것도 안 넣으면 줄 바꿈 처리
# print ("1111")
# print ("안녕하세요", end="")
# print ("코딩온입니다.")

# print ()
# print ("안녕하세요", end=", ")
# print ("코딩온입니다.")

# 변수 사용 예시
ive = "I AM"
print (ive)
ive = "장원영"
print (ive)
print (f"제가 좋아하는 가수는 {ive}입니다.")  # f 문자열 포매팅
print ("제가 좋아하는 가수는", ive, "입니다.", sep="")

# 자료형 확인
print (type(77))  # int: 정수
print (type(7.2))  # float: 실수

# 문자열 안의 따옴표 처리
print ('i\'ve')  # 작은 따옴표를 이스케이프 처리
print ("i've")  # 큰 따옴표를 사용해도 OK
print ("i\"ve")  # 큰 따옴표 안에서 이스케이프 처리
print ('i"ve')  # 작은 따옴표 안에서는 큰 따옴표 그대로 사용 가능


print ("111\n111")  # \n: 줄바꿈
print ("111\t111")  # \t: 탭 (8칸)

print (bin(10)) # 10진수 to 2진수
print (hex(10)) # 10진수 to 16진수
print (type(bin(10))) # 문자열
print (type(hex(10))) # 문자열열

print ("|\_/|")
print ("|q p|   /}")
print ('( - )"""\\')
print ('|"^"`   |')
print ("||_/=\\_ _|")

print (bin(10)) # 10진수 to 2진수
print (hex(10)) # 10진수 to 16진수
print (type(bin(10))) # 문자열
print (type(hex(10))) # 문자열열