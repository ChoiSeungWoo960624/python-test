import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path)

file_name = "연령별인구현황_성별.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")

# print(data.info())
# print(data.head())

region_name = input("검색하고 싶은 지역명을 입력하세요:  ")


for col in age_columns:
    new_func(data, col)
    
region_data = data[ data["행정구역"].str.contains(region_name)]

if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")
    exit()

#and를 이용하고 반복문 해야함
age_columns_ma = [col for col in region_data.columns if "세" in col and "남" in col]
age_columns_ra = [col for col in region_data.columns if "세" in col and "여" in col]
# print(age_columns)

'''
# 여기 데이터 타입이 여러개 일경우가 막혀 해결 방안을 모르겠어
def new_func(data, col):
    data[col] = data[col].str.replace("", ",", '').astype(int) #숫자랑 문자열이랑 섞여서 막혔던것...
'''
#해결 방안
male_result = (region_data[age_columns_ma].iloc[0].astype(str).str.replace(",", "").astype(int))
#iloc : serise에 백터화 연산을 적용하여 효율적이고 간결한 코드 작성이 가능
female_result = region_data[age_columns_ra].iloc[0].apply(lambda x : int(str(x).replace(",", "")))
# apply() : 사용자함수 정의의

age_groups_ma = [ col.split("_남_")[1] for col in age_columns_ma]
age_groups_ra = [ col.split("_여_")[1] for col in age_columns_ra]

#print(age_groups_ma)

#그래프 그리기

plt.figure(figsize=(10,))


plt.xlabel("연령대", fontproperties=font)
plt.ylabel("인구수", fontproperties=font)
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45, fontproperties=font)
plt.legend()
plt.show()