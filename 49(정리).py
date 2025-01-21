import math
import pandas as pd
'''
# 기존 데이터프레임
data = {
    "Name": ["홍길동", "임꺽정", "성춘향"],
    "age": [25, 30, 27],
    "Citt": ["서울", "부산", "인천"],
}
df = pd.DataFrame(data, index=["a", "b", "c"])

result = df.copy()

# loc를 사용하여 새 행 추가
result.loc["d"] = ["이몽룡", 31, "포항"]  # "Citt" 및 "agd"에 None 추가
result.loc["e"] = ["전우치", 28, "대전"]

print(result)
'''

'''
data = {
    "Name": ["홍길동", "임꺽정", "성춘향"],
    "Age": [25, 30, 27],
    "City": ["서울", "부산", "인천"],
}
df = pd.DataFrame(data, index=["a", "b", "c"])
# print(df)
# 데이터값 추출하는 방법########
# loc(index, column)
# print(df.loc["b"])
# print(df.loc["b", "Age"])
# print(df.loc["a":"c", "Name":"Age"])
# print(df.loc[~(df["Age"] >= 30)])
# print(df.loc[:, "Name"])
# print(df.loc["a", :])

# print(df.iloc[1])
# print(df.iloc[1, 1])
# print(df.iloc[0:2, 0:1])  # 끝값이 포함되지 않음
# print(df.iloc[[0, 2], [1, 2]])
# print(df.iloc[:, 0])
# print(df.iloc[0, :])
#############################

# 데이터를 넣고 추가/수정하는 방법#########
# 행추가
# new_data = {"Name": "이몽룡", "Age": 31, "City": "포항"}
# result = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
# print(result)

# 인덱스와같이 행추가
new_data = pd.DataFrame({"Name": "이몽룡", "Age": 31, "City": "포항"}, index=["d"])
# concat
result = pd.concat([df, new_data])
# loc
result.loc["e"] = ["전우치", 28, "대전"]
# print(result)

# 열추가
result["직업"] = ["엔지니어", "개발자", "디자이너", "기획자", "데이터분석가"]
# print(result)

# 요소값수정
result.at["b", "City"] = "천안"
result.loc[result["Name"] == "임꺽정", "Age"] = 31
print(result)

#컬럼값 변경
result.rename(columns={"Name": "이름", "Age": "나이", "City": "도시"}, inplace=True)
#inplace = True : 원본데이터 수정

#데이터정렬(기본:오름차순)
result.sort

print(result)
'''

#실습 2. 데이터프레임 만들기
data = {
    "이름": ["홍길동", "임꺽정", "성춘향"],
    "수학": [25, 30, 27],
    "영어": [88, 76, 89],
    "과학": [95, 89, 84],
}
df = pd.DataFrame(data, index=["0", "1", "2"])
result = df.copy()
result.loc[3] = ["이몽룡", 88, 85, 90]
result["Total"] = [268, 255, 254, 263]
result.rename(columns={"수학": "Math"}, inplace=True)
result.loc[result["영어"] == 76, "영어"] = 80
print(result)

