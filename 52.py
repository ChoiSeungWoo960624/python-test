import matplotlib.pyplot as plt
from matplotlib import font_manager #옵션 추가 - 한글 폰트는 눈누에서 다운받으면 됨

#폰트경로
path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc("font", family=font)
'''
#그래프 여러개 그리기
#1-1 한개의 창에 여러개 그리기
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]
plt.plot(x, y1, label="y=x", color="red")
plt.plot(x, y2, label="y=2x", color="orange")
plt.plot(x, y3, label="y=3x", color="green")
plt.plot(x, y4, label="y=4x", color="blue")

plt.legend(title="4graph", loc="upper center", ncol=4) #범례
plt.title("graph sample")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 1-2 하나씩 여러개 그리기 방법1
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("x=y")

plt.subplot(2, 2, 2)
plt.plot(x, y1)
plt.title("x=2y")

plt.subplot(2, 2, 3)
plt.plot(x, y1)
plt.title("x=3y")

plt.subplot(2, 2, 4)
plt.plot(x, y1)
plt.title("x=4y")

plt.suptitle("sample graph")
plt.tight_layout() #자동으로 간격조절
plt.show()


# 1-2 하나씩 여러개 그리기 방법2
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, y1) #axes변수 명
axes[0, 0].set_title("x=1y")

axes[0, 1].plot(x, y2)
axes[0, 1].set_title("x=2y")

axes[1, 0].plot(x, y3)
axes[1, 0].set_title("x=3y")

axes[1, 1].plot(x, y4)
axes[1, 1].set_title("x=4y")

plt.suptitle("sample graph")
plt.tight_layout()
plt.show()


# 수직 막대그래프
categories = ["A", "B", "C"]
values = [10, 15 ,7]

# plt.bar(categories, values, width=0.7, color=["r", "g", "b"], alpha=0.5, edgecolor="black", linewidth=2) # alpha= 선명도 ,aligh="edge"그래프가 출반선에 맞춤 
bars = plt.bar(categories, values, color="orange", label="Bar Graph")

#바그래프별 텍스트 넣기
for bar in bars:
#    plt.text( bar.get_x() + bar.get_width() / 2, bar.get_height() +0.5, str(bar.get_height()), ha="center", va="top", color="black",)
#bar.get_height() +0.5 y좌표 글 넣기 ,  bar.get_x() + bar.get_width() / 2 - x좌표 막대기 중심
    plt.text( bar.get_x() + bar.get_width() / 2, bar.get_height() +0.5, ["i", "helo", "me"], ha="center", va="top", color="black",)
plt.xticks(categories, ["2023", "2024", "2025"])

#기준선
plt.axhline(x=values[0], linestyle="--")

plt.title("Bar graph")
plt.show()
'''

#수평막대기
categories = ["A", "B", "C"]
values = [10, 15 ,7]

bars = plt.barh(categories, values, color="skyblue")

for bar in bars:
    plt.text( bar.get_width() +0.5, bar.get_y() + bar.get_height() / 2, str(bar.get_width()), ha="right", va="center", color="black")

plt.legend(bars, ["2023", "2024", "2025"], ncol=3)

#기준선
plt.axvline(x=values[0], linestyle="--")

plt.title("Bar graph", pad=10)
plt.xlabel("category")
plt.ylabel("year")
#plt.show()

#저장방법
plt.savefig("bar.jpg", format="jpg") #(제목, 형태태)

