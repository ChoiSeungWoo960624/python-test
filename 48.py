#pandas

from h11 import Data
import  pandas as pd

#리스트형식으로 생성
# data = [10, 20, 30, 40]
# series = pd.Series(data)
# print(series)

# data = [10, 20, 30, 40]
# # series = pd.Series(data) #기본인덱스
# series = pd.Series(data, index=["a", "b", "c", "d"]) # 커스텀 인덱스
# print(series)

#딕셔너리형식으로 생성
# data = {"a": 10, "b": True, "c": 3.14, "d": "Python"}
# series = pd.Series(data)
# print(data)
# print(series.index) #인덱스만 나오게 출력
# print(series.values) # 값만 나오게 출력
# print(series.shape) # 길이

# data = {"a": 10, "b": True, "c": 3.14, "d": "Python"}
# series = pd.Series(data, name="딕셔너리")
# print(data)
# print(series.index) #인덱스만 나오게 출력
# print(series.values) # 값만 나오게 출력
# print(series.shape) # 길이

# data = ('민지', '여', False)
# member = pd.Series(data, insex=["이름", "성별", "결혼여부"])
# print(member)
# print(member["이름"])
# print(member[["성별", "결혼여부"]])

data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])
#print(series["a"]) #인덱스를 변경했으면 그 인덱스를 그 인덱스를 사용(권장)
print(series[series > 20])
# """
# c    30
# d    40
# e    50
# dtype: int64
# """
# series["c"] = 100
# print(series)
# """
# a     10
# b     20
# c    100
# d     40
# e     50
# dtype: int64
# """
# print("a" in series) # 인덱스 "a"가 존재
# print(series.sum()) # 합계
# print(series.mearn()) #평균
# print(series.max()) # 최대값
# print(series.astype(float)) # 타입을 변경경

# #실습 1. 시리즈 만들기기
# data = ["4cups", "1cup", "2 larege", "1 can"]
# series = pd.Series(data, index=["밀가루", "우유", "계란", "참치캔"], name="Dinner")
# print(series)
