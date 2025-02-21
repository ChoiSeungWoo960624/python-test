import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# 이미지 로드
image = cv2.imread("diagram2.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise FileNotFoundError("이미지 파일을 찾을 수 없습니다. 경로를 확인하세요.")

# 이미지를 HSV로 변환 (사용되지 않지만 유지)
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 경계선을 가져오는 함수
def get_contours(img, min_area, is_simple=False):
    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 이진화 적용
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 근사화 방식 설정
    if is_simple:
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    result = []

    # 최소 면적 이상인 윤곽선만 선택
    for cnt in contours:
        if cv2.contourArea(cnt) > min_area:
            result.append(cnt)

    return result

FILTER_RATIO = 0.85

# 원형인지 여부를 판별하는 함수
def is_circle(cnt):
    cnt_length = cv2.arcLength(cnt, True)
    cnt_area = cv2.contourArea(cnt)

    # ratio가 1에 가까울수록 원형
    ratio = 4 * math.pi * cnt_area / pow(cnt_length, 2)

    return ratio > FILTER_RATIO

# 꼭짓점을 그리는 함수
def draw_points(img, cnt, epsilon, color):
    cnt_length = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon * cnt_length, True)

    for point in approx:
        cv2.circle(img, (point[0][0], point[0][1]), 3, color, -1)

# 그레이스케일 변환 후 이진화
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 윤곽선 찾기 (이진화된 이미지 사용)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 윤곽선 그리기
for contour in contours:
    if cv2.contourArea(contour) > 100:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    
    # 윤곽선 박스
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# OpenCV 창에서 결과 출력
cv2.imshow("Original Image with Bounding Boxes", image)
cv2.imshow("Threshold Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Matplotlib 출력 (필요하면 사용)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Contours")
plt.show()