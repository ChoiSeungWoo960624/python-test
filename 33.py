#파일 입출력
#파일 쓰기
'''
with open("text.txt1", "w") as file:
    file.write("안녕하세요\n") # 붙여 나오기때문에 \n해서 만들기
    file.write("파이썬파일 쓰기 연습\n")


with open("text.txt2", "w", encoding="utf-8") as file: # 깨져서 나오기 때문에 encoding써서 방지
    file.write("안녕하세요\n") # 붙여 나오기때문에 \n해서 만들기
    file.write("파이썬파일 쓰기 연습\n")

#내용추가
with open("text.txt2", "w", encoding="utf-8") as file:
    file.write("내용추가\n")
    file.write("11111")


#writelines()
lines = ["첫번째내용\n", "두번째내용\n", "세번째내용\n"]

with open("test2.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)


#사용자로부터 입력 받은 내용을 파일로 만들기
with open("user.txt", "w", encoding ="utf-8") as file:
    while True:
        line = input("파일에 넣을 문자열입력(종료하려면 '종료' 압력)")
        if line == "종료":
            print("\n입력을 종료합니다")
            break

        file.write(line + "\n")


# 파일 읽기
with open("33-(사용자로부터)user.txt", "r", encoding="utf-8") as file:
    print(file.read()) #파일 전체 읽기

with open("33-(사용자로부터)user.txt", "r", encoding="utf-8") as file:
    print(file.readline()) #파일 한줄씩 읽기
    print(file.readline())

with open("test.")




with open("33-(사용자로부터)user.txt", "r", encoding="utf-8") as file:
    line = file.feadline()
    while line:
        print(line.strip())
        line = file.readline()

str = "                    문자열                        "
print(f"[{str.strip()}]")  # 양쪽공백제거
print(f"[{str.rstrip()}]")  # 우측공백제거
print(f"[{str.lstrip()}]")  # 좌측공백제거
'''

# enumerate() # 리스트를 튜플형태로 반환, 반환값이 두개
from multiprocessing import Value


with open("33-(사용자로부터)user.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    # (0, "집가고 싶다. 배고프다 배아프다 졸리다 집가고싶다.\n"), (1, 살려줘)  <- [""집가고 싶다. 배고프다 배아프다 졸리다 집가고싶다.\n", "살려줘\n"]
    for idx, Value in enumerate(lines):
        print(f"{idx}인덱스의 값은 {Value.strip()}입니다.")
'''
0인덱스의 값은 집가고 싶다. 배고프다 배아프다 졸리다 집가고싶다.입니다.
1인덱스의 값은 살려줘입니다.
2인덱스의 값은 운동가기싫다입니다.
3인덱스의 값은 아아아ㅏ앙앙입니다.
'''

