import cv2
from matplotlib import axes, contour
import matplotlib.pyplot as plt
import numpy as np
from streamlit import image

# #스킨 검출
# image = cv2.imread("jo-skin.jpg")
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# #피부색 범위
# #H : 0 ~ 20, S: 48 ~ 255, V: 80~255
# lower = np.array([0, 48, 80])
# upper = np.array([20, 255, 255])

# mask = cv2.inRange(hsv, lower, upper)

# #노이즈제거
# kernel = np.ones((5, 5), np.uint8)

# # 침식 연산
# mask_eroded = cv2.erode(mask, kernel, iterations=1)

# # 팽창 연산
# mask_dilated = cv2.dilate(mask, kernel, iterations=1)

# #커누어 윤곽선
# #우리가 원하는 영역 => 마스크된 부분
# contours, _ = cv2.findContours(mask_eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# #원본이미지에 윤곽선을 그리기
# image_copy = image.copy()
# cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 4)

# fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# axes[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# axes[0, 0].set_title("orginal")
# axes[0, 0].axis("off")

# axes[0, 1].imshow(mask, cmap="gray")
# axes[0, 1].set_title("mask")
# axes[0, 1].axis("off")

# axes[1, 0].imshow(cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB))
# axes[1, 0].set_title("erode")
# axes[1, 0].axis("off")

# plt.tight_layout()
# plt.show()


import cv2
import numpy as np

# 웹캠 연결
cap = cv2.VideoCapture(0)

# 피부색 범위 (HSV)
lower = np.array([0,0, 40])
upper = np.array([20, 205, 205])

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # BGR -> HSV 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 피부색 마스크 생성
    mask = cv2.inRange(hsv, lower, upper)

    # 노이즈 제거 (침식 & 팽창)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)

    # 윤곽선 찾기
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 윤곽선 그리기
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # 작은 영역 무시
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)

    # 화면 출력
    cv2.imshow("Skin Detection", frame)
    cv2.imshow("Mask", mask)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()