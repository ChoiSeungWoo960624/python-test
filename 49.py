#DataFrame(데이터 프레임)
from h11 import Data
import  pandas as pd

data = {
    "Name" : ["홍길동", "임꺽정", "성춘향"],
    "age": [25, 30, 27],
    "Citt": ["서울", "부산", "인천"],
}


df = pd.DataFrame(data)
#print(df)
"""
  Name  age Citt
0  홍길동   25   서울
1  임꺽정   30   부산
2  성춘향   27   인천
"""
df = pd.DataFrame(data, index=["a", "b", "c"])
#print(df)
"""
  Name  age Citt
a  홍길동   25   서울
b  임꺽정   30   부산
c  성춘향   27   인천
"""
# print(df.loc["b"])
# print(df.loc["b", "age"])
# print(df.loc["a":"c", "Name":"age"]) #a~c까지 , 칼럼값가져오기
# print(df.loc[(df["age"] >= 30)]) #>= 30 30세이상만 가져오겠다.
# print(df.loc[~(df["age"] >= 30)]) # 30세 미만으로 가져오겠다.
# print(df.loc[:, "Name"]) #이름에 있는것만 출력력
#print(df.loc["a", :]) a데이터만 가져오기

#print(df.iloc[1])
#print(df.iloc[1, 1]) 임꺽정의 나이를 출력
#print(df.iloc[0:2, 0:1]) # 끝값이 포함되지 않음
"""
   Name  age
a  홍길동   25
b  임꺽정   30
c  성춘향   27
 Name
a  홍길동
b  임꺽정
 """
#print(df.iloc[[0, 2], [1, 2]])
"""
   age Citt
a   25   서울
c   27   인천
"""
# print(df.iloc[:, 0])
# print(df.iloc[0, :]) #0의 전체

#데이터를 넣고 추가/수정하는 방법#####
#행추가
new_data = {'Name': "이몽룡", "agd": 31, "city": "포항"}
# result = pd.concat([df, pd.DataFrame([new_data])])
# #concat 배열함수
# print(result)
"""
  Name   age Citt   agd City
a  홍길동  25.0   서울   NaN  NaN
b  임꺽정  30.0   부산   NaN  NaN
c  성춘향  27.0   인천   NaN  NaN
0  이몽룡   NaN  NaN  31.0   포항
"""
result = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
#concat 배열함수
print(result)

# 인덱스와 같이 추가
new_data = pd.DataFrame({"Name": "이몽룡", "age": 31, "city": "포항"}, index=["d"]) #d는 리스트 형태이며, []넣어야함
#concat
result = pd.concat([df, new_data])

#loc로 하는 방법
# data = {
#     "Name": ["홍길동", "임꺽정", "성춘향"],
#     "age": [25, 30, 27],
#     "city": ["서울", "부산", "인천"],
# }
# df = pd.DataFrame(data, index=["a", "b", "c"])

# 새 데이터 추가
new_data = pd.DataFrame({"Name": ["이몽룡"], "age": [31], "city": ["포항"]}, index=["d"])
result = pd.concat([df, new_data])  # ignore_index=True 제거

# loc로 새로운 데이터 추가
result.loc["e"] = ["전우치", 28, "대전"]  # 문자 인덱스 추가
# print(result)


# # 열추가
result["직업"] = ["엔지니어", "개발자", "디자이너", "기획자", "데이터분석가가"]
# print(result)

# 요소값수정
result.at["b", "city"] = "천안"
result.loc[result["name"] == "임꺽정", "age"] = 36
print(result)
