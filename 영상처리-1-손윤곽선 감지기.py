import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
# 웹캠 연결
cap = cv2.VideoCapture(0)

# 캠이 없을 경우 조건문 만들기
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# matplotlib 인터렉티브 모드 활성화 (실시간 업데이트)
plt.ion()  # 인터렉티브 모드 활성화

while cap.isOpened():
    ret, frame = cap.read()  # ret : True or False
    if not ret:
        print("프레임을 읽지 못했습니다.")
        break  # 프레임을 읽지 못하면 while문 종료
    
    # matplotlib 3개의 영상 실시간 업데이트
    plt.clf()  # 이전 그림을 지우고 새로운 그림을 그리기

    # 원본 이미지
    original = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 4))  # 크기 설정
    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.axis("off")  # 축 제거
    plt.title("Original")  # 제목 설정

    # 손 윤곽선 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # 이진화 처리
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 윤곽선 검출
    contour_img = frame.copy()  # 원본을 복사해서 사용
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 3)  # 윤곽선 그리기
    contour_img = cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 3, 2)
    plt.imshow(contour_img)
    plt.axis("off")
    plt.title("Contour")

    # 샤프닝 커널 정의
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # 필터 적용
    sharpened = cv2.filter2D(contour_img, -1, kernel)

    plt.subplot(1, 3, 3)
    plt.imshow(sharpened)
    plt.axis("off")
    plt.title("Sharpened")

    # 실시간 업데이트를 위한 간격 설정
    plt.pause(0.01)  # 10ms 동안 잠시 멈추고 화면 업데이트

# 종료 처리
cap.release()  # 영상 해제
cv2.destroyAllWindows()  # 모든 윈도우 제거
plt.close('all')  # 모든 matplotlib 창 닫기
'''

plt.ion()  # matplotlib 인터렉티브 모드 활성화(실시간 업데이트)

# 종료 플래그
quit_cap = False


# matplotlib 이벤트 핸들러
def on_key(e):
    global quit_cap
    if e.key == "q":
        quit_cap = True


plt.figure(figsize=(12, 4))
# 키이벤트 연결
plt.gcf().canvas.mpl_connect("key_press_event", on_key)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열수없습니다.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # matplotlib 3개의 영상 실시간 업데이트
    plt.clf()  # 기존의 그래프 초기화

    # 원본
    original = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 예시로 이미지를 제출할때
    cv2.imwrite("orginal.jpg", cv2.cvtColor(original, cv2.COLOR_RGB2BGR))

    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title("original")
    plt.axis("off")

    # 손 윤곽선 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # 이진화처리
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )  # 컨투어탐지
    contour_img = frame.copy()  # 원본을 복사해서 사용
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)  # 컨투어 그리기
    contour_img = cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 3, 2)
    plt.imshow(contour_img)
    plt.title("contour")
    plt.axis("off")

    # 샤프닝 필터 적용
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(contour_img, -1, kernel)

    plt.subplot(1, 3, 3)
    plt.imshow(sharpened)
    plt.title("sharp")
    plt.axis("off")

    # 업데이트 간격을 조절
    plt.pause(0.01)
    plt.show()

    # # 종료
    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break
    if quit_cap:
        print("종료합니다")
        break

cap.release()
cv2.destroyAllWindows()
plt.close("all")  # 모든 matplotlib 닫기