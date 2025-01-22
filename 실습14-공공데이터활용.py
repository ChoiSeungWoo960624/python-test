#실습. 공공데이터 활용
from operator import eq
import pandas as pd

file_name = "서울시 공원 내 운동기구 설치 현황_201231.csv"
df = pd.read_csv(file_name, encoding="cp949")

#print(df.head())
#print(df.info())
df.columns = df.columns.str.strip() #df.columns 열이름 나타내는 index
#print(df.columns)

# 공원별 총 운동기구 설치 수
park_eq = df.groupby('구분')['운동기구 수량'].sum().reset_index()
#print("공원별 총 운동기구 설치 수:")
#print(park_eq)

# 운동기구 종류별 설치 개수
eq_count = df.groupby('운동기구 기종명')['운동기구 수량'].sum().reset_index()
#print("\n운동기구 종류별 설치 개수:")
#print(eq_count)

# 관리기관별 총 운동기구 설치 수
code_eq = df.groupby('관리기관')['운동기구 수량'].sum().reset_index()
#print("\n관리기관별 총 운동기구 설치 수:")
#print(code_eq)

# 특정 공원 데이터 필터링 (예: 중랑캠핑숲)
sp_park = df[df['구분'] == '중랑캠핑숲']
print("\n특정 공원 데이터 (중랑캠핑숲):")
print(sp_park)

# 특정 운동기구 종류 데이터 필터링 (예: 스텝사이클)
sp_eq = df[df['운동기구 기종명'] == '스텝사이클']
print("\n특정 운동기구 종류 데이터 (스텝사이클):")
print(sp_eq)

# 운동기구 수량 기준 내림차순 정렬
eq_co_sp = df.sort_values(by='운동기구 수량', ascending=False)
print("\n운동기구 수량 기준 내림차순 정렬:")
print(eq_co_sp)