import matplotlib.pyplot as plt
'''
#히스토그램 데이터 분포용 ex. 통계 주사위던지기, 로또 번호
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 5, 5]

plt.hist(data, color="green", histtype="bar", bins=11) #bins - 구간의 간격격

plt.title("hist")
plt.xlabel("value")
plt.ylabel("bins")
plt.show()


#여러개 data
data1 = [1, 2, 2, 3, 3, 3, 4]
data2 = [2, 3, 3, 4, 4, 4, 5]

plt.hist([data1, data2], bins=7, color=["green", "purple"], label=["data1", "data2"])
plt.title("hist")
plt.xlabel("value")
plt.ylabel("bins")
plt.legend() #범례용
plt.show()


#산점도
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [20, 50, 80, 100, 200]
colors = [10, 20, 30, 40, 50]

plt.scatter(x, y, s=sizes, c=colors, cmap="viridis") #camp - 색상구분
plt.colorbar(label="color bar") #colorbar - 오른쪽나오는 바

plt.show()


import numpy as np

n = 50
x = np.random.rand(n) # 0과 1의 난수
y = np.random.rand(n)

area = (30 * np.random.rand(n)) **2 # 0과 30사이 난수생성 후 제곱
colors = np.random.rand(n)

plt.scatter(x, y, s=area, c=colors, cmap="Spectral", alpha=0.6)
plt.show()


#파이차트
sizes = [25, 25, 20, 20]
labels = ["A", "B", "C", "D"]

plt.pie(sizes, labels=labels)
plt.show()

'''
#파이차트2
# sizes = [15, 30, 24, 10]
# labels = ["Apple", "Banana", "Cherry", "grape"]
# explode = [0, 0.1, 0, 0]
# colors = ["pink", "lightblue", "yellow", "blue"]

# plt.pie(sizes, labels=labels, explode=explode, autopct="%1.1f%%", shadow=True, startangle=140, colors=colors) #startangle =첫 번째 파이 조각이 12시 방향에서 시계 방향으로 140도 회전한 위치에서 시작.
# plt.show()


# #도넛

# sizes = [40, 30, 20, 10]
# labels = ["x", "Y", "z", "w"]

# # Create the donut chart
# plt.pie(
#     sizes, 
#     labels=labels, 
#     wedgeprops={"width": 0.4}
# )

# plt.show()