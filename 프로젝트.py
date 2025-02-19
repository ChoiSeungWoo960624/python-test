# 주 스크립트 입니다. 테스트 기능은 새 py파일로 안정성 확인 후 추가해주세요.
import pandas as pd
file_name="Data/pm2301.csv"
data=pd.read_csv(file_name, encoding="EUC-KR")

region_data=data[data["망"].str.contains("도시대기", na=False)][data["지역"].str.contains("서울 서초구",na=False)]
# print(region_data)

PM25_data=region_data.dropna(subset=['PM25'])
# print(deleted_data)

fixed_data=PM25_data[data["측정일시"].astype(str).str.contains("202301",na=False)]
print(fixed_data)

Seoul2301_avg = fixed_data['PM25'].mean().round(4)
print(Seoul2301_avg)

Busan = fixed_data['PM25'].mean().round(4)

# 데이터 전처리 해야함 (Todo)


"""
지역별로 나누되 날짜별로 전처리
양식 : Seoul2301 [Seoul = 지역명을 영어로, 2301 = 23(연도)01(월)]
지역 : 서울, 경기, 대구, 경북, 부산,경남
"""