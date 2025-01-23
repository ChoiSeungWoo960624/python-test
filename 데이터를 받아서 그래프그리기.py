import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager


#한글설정
path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path)

file_name = "연령별인구현황_월간.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")

# print(data.info())
# print(data.head())

region_name = input("검색하고 싶은 지역명을 입력하세요:  ")

#원하는 데이터만 추출
age_columns = [col for col in data.columns if "세" in col] #세라고 붙은 애들만 추출
#print(age_columns)

#문자열을 숫자열로 바꾸기
for col in age_columns:
    data[col] = data[col].str.replace(",", "").astype(int)

#필터링
#메서드 contains() : 문자열 데이터 필터링, 특정 패턴을 찾을 때
#옵션값
# na : 결측값을 포함할지 결정, 기본값은 True
# case : 영문의 대소문자를 구분, 기본값 True
region_data = data[data["행정구역"].str.contains(region_name)]

#예외 처리
if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

#데이터 가져오기
#2024년12월_계_0~9세 -> 0~9세만 나오게
age_groups = [ col.split("_계_")[1] for col in age_columns] # ["2024년 12월", 0,9세]로 나눠지는데 나는 1번째 자료가 필요하니 [1]넣기

#결과 값
result = region_data[age_columns].iloc[0].values

print(result)
'''
검색하고 싶은 지역명을 입력하세요:  동대문구
[17174 22270 55543 50145 47253 51914 48622 29361 14531  1872    50]
'''

# 그래프그리기
plt.figure(figsize=(10, 8))
plt.plot(age_groups, result, marker="o", label=region_name)
plt.title(f"{region_name}의 연령별 인구 수", fontsize=16, pad=10, fontproperties=font)
plt.xlabel("연령대", fontproperties=font)
plt.ylabel("인구수", fontproperties=font)
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45, fontproperties=font)
plt.legend()
plt.show()