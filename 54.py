import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#seaborn에 들어간 데이터 셋
#print(sns.get_dataset_names())

#예제데이터
#tips = sns.load_dataset("tips")
#print(tips.head())

#sns.scatterplot(x="total_bill", y="tip", data=tips, hue="size", palette="deep", style="time", size="size")

#단순데이터 분포 확인 stripplot
#sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, hue="size", dodge=True)

#swarmplot - jitter가 없음
#sns.swarmplot(x="day", y="total_bill", data=tips, hue="size", dodge=True)

#relplot 관계형 플롯
#sns.relplot(x="total_bill", y="tip", data=tips, style="time", hue="day") #hue애 데이터 넣는 순간 day와 색을 넣어줌

#catploy 카테고리형 데이터의 분포
#sns.catplot(x="day", y="total_bill", data=tips, kind="violin", hue="day")

# displot  데이터의 분포를 시각화
#sns.displot(tips["total_bill"], bins=30)

#pairplot 여러 변수 간의 관계를 한 번에 시각화
#sns.pairplot(data=tips, hue="time")

#회귀선이 포함된 산점도를 생성
#sns.regplot(data=tips, x="total_bill", y="tip")

#2차원 데이터(매트릭스)를 히트맵 형태로 시각화.
# data = np.random.rand(10, 10)
# sns.heatmap(data, annot=True, fmt=".2f") 



#실습 1
# tips = sns.load_dataset("penguins")
# sns.scatterplot(x="bill_length_mm", y="bill_depth_mm", hue="species", alpha=0.6, data=tips)
# sns.catplot(x="species", y="body_mass_g",kind="bar", data=tips)
# sns.catplot(x="island", y="body_mass_g",kind="violin", data=tips)

# #실습 2
tips = sns.load_dataset("flights")
print(tips.info())

'''
#평균값 구하기
avg = tips.groupby("year")["passengers"].mean()
쓸 수 있는 값 변화시키기
avg = tips.groupby("year")["passengers"].mean().reset_index()
reset_index(): 인덱스를 초기화, 기존 인덱스를 데이터프레임의 열로 변환
'''
#2-1
avg = tips.groupby("year")["passengers"].mean().reset_index()
plt.plot(avg["year"], avg["passengers"])

#2-2
#pivot() : 데이터를 재구조화, index, column, value
pivot = tips.pivot(index="month", columns="year", values="passengers")
sns.heatmap(pivot, annot=True, fmt="d")

#3
year_1958 = tips[tips["year"] == 1958]
sns.barplot(x="month", y="passengers", data=year_1958)

plt.show()




#실습 3
tips = sns.load_dataset("titanic")
#sns.catplot(x="class", y="survived", data=tips, kind="point")
df = tips
sns.kdeplot(data=tips, x="age", hue="survived", multiple="stack")



plt.show()