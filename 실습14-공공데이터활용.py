#실습. 공공데이터 활용
import pandas as pd

file_name = "서울시 공원 내 운동기구 설치 현황_201231.csv"
df = pd.read_csv(file_name, encoding="cp949")

print(df.head())
print(df.info())
df.columns = df.columns.str.strip() #df.columns 열이름 나타내는 index
print(df.columns)


# 공원별 총 운동기구 설치 수

# 운동기구 종류별 설치 개수
# 관리기관별 총 운동기구 설치 수
# 특정 공원 데이터 필터링(예:중랑캠핑숲)
# 특정 운동기구 종류 데이터 필터링(예:스텝사이클)
# 운동기구 수량기준 내림차순 정렬
# 운동기구 수량기준 올림차순 정렬렬