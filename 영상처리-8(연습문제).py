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

"""
솔루션
import cv2
import numpy as np

image = cv2.imread("green.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([50, 100, 100])
upper = np.array([70, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

# result = cv2.bitwise_and(image, image, mask=mask)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count = 0
for contour in contours:
    # contourArea : 위에서 검출한 윤곽선의 면적을 계산하는 함수. 반환값은 면적을 float형식
    area = cv2.contourArea(contour)
    if area > 100:  # 작은 노이즈 제거
        count += 1
        x, y, w, h = cv2.boundingRect(
            contour
        )  # 객체를 감싸는 가장 작은 축에 정렬된 사각형
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(f"검출된 초록색은 : {count}개")
cv2.imshow("green", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""