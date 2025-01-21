import pandas as pd
#결측값
data = {
    "Name": ["홍길동", "임꺽정", "성춘향"],
    "Age": [25, None, 20],
    "City": ["서울", "부산", None],
}

df = pd.DataFrame(data)
print(df.isnull()) # 결측값 여부
print(df.isnull().sum()) #결측값갯수의 합
"""
Name    0
Age     1
City    1
"""
print(df.info())
'''
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    3 non-null      object
 1   Age     2 non-null      float64
 2   City    2 non-null      object
dtypes: float64(1), object(2)
memory usage: 204.0+ bytes
None
'''
# df_drop = df.dropna() #결측값있는 행을 모두 제거
# dr_drop_colum = df.dropna(axis=1) # 결측값이 있는 열들을 삭제
# df_fill = df.fillna(0)
# df_fill_prev = df.fillna(method="ffill") #이전에 있는 값으로 채움
df_fill_next = df.fillna(method="bfill")  # 다음에 있는 값으로 채움
print(df_fill_next)

#주요메서드
#inin()
s = pd.Series(["홍길동", "임꺽정", "성춘향", "이몽룡"])
result = s.isin(["홍길동", "이몽룡"])
print(result)

data = {
    'Name': ["홍길동", "임꺽정", "성춘향", "이몽룡"],
    "Age": [25, 30, 45, 20]
}
df = pd.DataFrame(data)
#result = df.isin(["성춘향", "홍길동", 20]) #True / False 찾기
result = df[df["Name"].isin(["성춘향", "홍길동", 20])] # True 값만 필터링
#print(result)

s = pd.Series([1, 2, None])
result = s.isin([None, 2])
#print(result)
'''
None
0     True
1    False
2    False
3     True
dtype: bool
0    False
1     True
2    False
dtype: bool
'''

# value_counts() 빈도수 체크 value_counts(옵션 넣기 가능)
# value_counts(normalize=True) #빈도를 비율 (%)
s = pd.Series(["사과", "바나나", "사과", "오렌지", "바나나", "사과"])
#print(s.value_counts())
'''
사과     3
바나나    2
오렌지    1
Name: count, dtype: int64
'''

df = pd.DataFrame(
    {
        "과일": ["사과", "바나나", "사과", "오렌지", "바나나", None, "사과"],
        "수량": [1, 2, 3, 4, 5, 6, 7]
    }
)
# print(df["과일"].value_counts(normalize=True))  # 빈도를 비율(%)
# print(df["과일"].value_counts(ascending=True))  # 오름차순
# print(df["과일"].value_counts(dropna=False))

# agg() 요약해서 알려줌
s = pd.Series([1, 2, 3, 4, 5])
result = s.agg(["sum", "mean", "max"])
# print(result)

df = pd.DataFrame({"A": [1, 2, 3], "B": [10, 11, 12]})
# print(df.agg(["sum", "mean"]))
print(df.agg({"A": "sum", "B": "mean"}))
#({"a": "sum", "b":"mean"}) a는 합만 b는 나누기만


#연산
# s1 = pd.Series([10, 20, 30])
# s2 = pd.Series([5, 15, 25])

# print(s1 + s2)
# print(s1 - s2)
# print(s1 * s2)
# print(s1 / s2)
# print(s1 > 15) # 15이상이면 True 미만이면 False

#통계연산
# print(s1.sum())
# print(s1.mean()) # 평균
# print(s1.max())
# print(s1.min())
# print(s1.std()) # 표준편차
# print(s1.ver()) # 분산
# print(s1.median()) # 중앙값

# #통계지표
# print(s1.describe()) #count, mean, std, min 25% 50% 75% max값을 출력해줌

#그룹
data = {
    "group": ["A", "A", "B", "B", "C"],
    "value": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
result = df.groupby("group")["value"].max()
'''
group
A    20
B    40
C    50
'''
print(result)

data = {
    "group": ["A", "A", "B", "B", "C"],
    "value1": [10, 20, 30, 40, 50],
    "value2": [5, 15, 25, 35, 45],
}
df = pd.DataFrame(data)
# result = df.groupby("group").agg({"value1": "sum", "value2": ["mean", "max"]})

result = df.groupby("group").filter(lambda x: x["value1"].sum() > 30)
print(result)