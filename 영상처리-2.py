import cv2
from matplotlib import axes
import matplotlib.pyplot as plt
import numpy as np
from streamlit import image

'''
# HSV 색상(Hue), 채도(Saturation), 명도(Value)
image = cv2.imread("jeju.jpg")

# BGR -> HSV 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


cv2.imshow("hsv", hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 색상범위 설정(빨강색)
lower = np.array([0, 120, 70])
upper = np.array([10, 255, 255])

"""
색상 범위 
빨강
(-10, 100, 100) ~ (10, 255, 255)
파랑색
(110, 100, 100) -> (130, 255, 255)
녹색
(50, 100, 100) -> (70, 255, 255)
"""


# 마스크생성
mask = cv2.inRange(hsv_image, lower, upper)

# 원본이미지에 마스크 적용
result = cv2.bitwise_and(image, image, mask=mask)

plt.figure(figsize=(12, 6))

#원본
plt.subplot(1, 2, 1)
plt.title("original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

#마스크
plt.subplot(1, 3, 1)
plt.title("result")
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis("off")

# 결과
plt.subplot(1, 3, 3)
plt.title("result")
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
'''

#erode, dilate
image = cv2.imread("jeju.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#       H(색상), S(채도), V(명도)
lower = np.array([100, 150, 0]) # 색상 범위의 최소값 (HSV)
upper = np.array([140, 255, 255]) # 색상 범위의 최대값 (HSV)

#마스크 생성
mask = cv2.inRange(hsv, lower, upper)

#커널
kernel = np.ones((5, 5), np.uint8)

#침식연산: 작은 노이즈제거 등, 객체의 경계를 줄임
mask_eroded = cv2.erode(mask, kernel, iterations=1) #None : 3*3 기본 커널

#팽창연산 : 객체의 경계를 확장하거나 침식 후 복원
mask_dilated = cv2.dilate(mask, kernel, iterations=1)

'''
# 1
plt.figure(figsize=(12, 6))
plt.subplot(1, 4, 1)
plt.title("original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 4, 2)
'''

#2 다르게 표현
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title("orginal")
axes[0, 0].axis("off")

axes[0, 1].imshow(mask, cmap="gray")
axes[0, 1].set_title("mask")
axes[0, 1].axis("off")

axes[1, 0].imshow(mask_eroded, cmap="gray")
axes[1, 0].set_title("erode")
axes[1, 0].axis("off")

axes[1, 1].imshow(mask_dilated, cmap="gray")
axes[1, 1].set_title("dilate")
axes[1, 1].axis("off")

plt.tight_layout()
plt.show()