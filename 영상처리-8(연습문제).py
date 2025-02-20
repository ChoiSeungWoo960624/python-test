import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 로드
image = cv2.imread("lol.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise FileNotFoundError("이미지 파일을 찾을 수 없습니다. 경로를 확인하세요.")

# BGR에서 HSV로 변환
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 초록색 범위 정의
lower_green = np.array([40, 80, 80])
upper_green = np.array([60, 255, 255])  

# 초록색 영역을 마스크로 추출
mask = cv2.inRange(img_hsv, lower_green, upper_green)

# 윤곽선 찾기
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 윤곽선 그리기

for contour in contours:
    if cv2.contourArea(contour) > 500:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    
    # 윤곽선 박스
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# OpenCV 창에서 결과 출력
cv2.imshow("Original Image with Bounding Boxes", image)
cv2.imshow("Green Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.show()