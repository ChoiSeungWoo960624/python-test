import matplotlib.pyplot as plt
from matplotlib import font_manager #옵션 추가 - 한글 폰트는 눈누에서 다운받으면 됨

#폰트경로
path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc("font", family=font)

#기본 사용법
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#plt.plot(x, y) #plot 기본으로 그려주는 그래프
plt.plot(x, y, color="red", linestyle="--", linewidth=3, label="Samle graph") # 옵션추가가 linestyle - 선스타일 바낄 수 있음, linewidth - 선두께께

plt.plot(
    x,
    y,
    marker="*",
    markersize=20,
    markerfacecolor="red",
    markeredgecolor="blue",
    label="marker sample",
)  # 마커표시plt.title("Title")

font = {
    "size": 20,
    "color": "white",
    "backgroundcolor": "black",
    "weight": "bold",
}  # 폰트설정

# plt.title("Matplotlib", pad=10, fontsize=20, color="white", backgroundcolor="green") # 풀어쓰는방법
plt.title("Matplotlib Dict", pad=10, fontdict=font)  # 딕셔너리 이용방법
#pad 제목이랑 표 사이 간격


#plt.grid(True) #뒷 배경에 격자 생김
plt.grid(True, axis="both", linestyle="--", color="blue", alpha=0.2) #x,y 같이하고 싶다 both x만 하고싶으면 'x'만 넣기기, alpha - 선명도차이 
plt.legend(title="legend", fontsize=13, loc="lower center") #범례 표시

# x, y축 레이블
plt.xlabel("x axis", fontdict=font, labelpad=10) #labelpad - 그래프와 x축 제목 사이간격 
plt.ylabel("y axis", fontdict=font)

#축범위설정
plt.xlim([1, 10]) #1~5까지였는데 축을 10까지 늘림 그래프는 변화 x
plt.ylim([0, 20]) # 0부터 시작해서 20까지 나옴 그래프는 변화 x
plt.axis([1, 10, 0, 20]) # 앞에 x축 미니 맥, 뒤에는 y축 미니 맥
plt.axis("equal") # x축과 y축을 동일하게 설정
plt.axis("tight") # 그래프가 모든 영역에 딱 맞춰서 설정
plt.axis("scaled") # 데이터의 비율에 따라서 설정
plt.axis("auto") # 자동으로 맞춰줌

plt.show()


