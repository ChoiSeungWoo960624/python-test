""" 
실습 open cv 이미지에서 원 or 사각형 검출
import os
import math
import cv2
import numpy as np

# 이미지 로드
path = os.path.join('diagram.jpg')
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 노이즈 제거를 위한 블러 적용
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 이진화 적용
ret, thr = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# 윤곽선 검출
contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def drawShape(img, pts):
    (x, y, w, h) = cv2.boundingRect(pts)

    # 전체를 감싸는 경우 무시
    if w * h > (image.shape[0] * image.shape[1]) * 0.8:
        return

    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)  # 사각형

# 도형 검출
for cont in contours:
    approx = cv2.approxPolyDP(cont, cv2.arcLength(cont, True) * 0.02, True)
    vtc = len(approx)

    # 사각형 판별
    if vtc == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h  # 가로/세로 비율 계산

        if 1 <= aspect_ratio <= 1:  # 정사각형에 가까운 경우
            drawShape(image, cont)
        else:
            drawShape(image, cont)

    # 원 판별
    else:
        area = cv2.contourArea(cont)

        # 면적이 너무 작으면 무시
        if area < 550:
            continue

        (x, y), radius = cv2.minEnclosingCircle(cont)

        if area > 0:
            ratio = (radius ** 2) * math.pi / area
            if 1.0 <= ratio <= 1.2:
                drawShape(image, cont)

# 결과 출력
cv2.imshow('Detected Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#open cv 얼굴이나 특정 객체를 감지한 후, 해당 영역에 모자이크 효과(블러 처리) 적용
import cv2

# 얼굴 및 눈 탐지기 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# 웹캠 연결
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 찾을 수 없습니다.")
    exit()

def apply_mosaic(img, x, y, w, h, ratio=0.05):
    roi = img[y:y+h, x:x+w]  # 얼굴 영역 추출
    h, w = roi.shape[:2]

    # 축소 후 확대하여 모자이크 효과 적용
    small = cv2.resize(roi, (int(w * ratio), int(h * ratio)), interpolation=cv2.INTER_AREA)
    mosaic = cv2.resize(small, (w, h), interpolation=cv2.INTER_AREA)

    img[y:y+h, x:x+w] = mosaic  # 원본 이미지에 적용

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 탐지
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for x, y, w, h in faces:
        apply_mosaic(frame, x, y, w, h)  # 모자이크 적용

        # 눈 탐지
        face_roi = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_roi, scaleFactor=1.1, minNeighbors=7, minSize=(15, 15))
        
        # 눈 감지 시 파란색 사각형
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (255, 0, 0), 2) 

    cv2.imshow("Face Mosaic", frame)

    # 종료 (q 키 누르면 종료)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


#open cv 사용자가 마우스로 클릭한 위치에 원을 그리고 드래그하면 선을 그릴 수 있도록하기기

import numpy as np
import cv2

windowName = 'Drawing'
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(windowName)
green = (0, 255, 0)
red = (0, 0, 255)

drawing = False
(ix, iy) = (-1, -1)

def draw(event, x, y, flags, param):
    global ix, iy, drawing
    
    # 왼쪽 마우스 버튼이 눌러졌을 때 원 그리기
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        cv2.circle(img, (ix, iy), 25, red, -1)
    
    # 마우스를 드래그하면 선 그리기
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img, (ix, iy), (x, y), green, 2)
            ix, iy = x, y
    
    # 왼쪽 마우스를 뗄 때 종료
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.setMouseCallback(windowName, draw)

def main():
    while True:
        cv2.imshow(windowName, img)
        # ESC 키를 누르면 종료
        key = cv2.waitKey(1)
        if key == 27:  
            break
            
    cv2.destroyAllWindows()

main()
"""

#opencv 마우스를 움직이면 해당 위치 주변이 확대되는 효과
import cv2
import numpy as np

image = cv2.imread('KakaoTalk_20250220_155201993.jpg')

h, w, _ = image.shape

# 돋보기 크기
zoom_size = 100  # 확대할 영역 크기
scale_factor = 2  # 확대 배율

# 마우스
def zoom_effect(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # 확대할 영역 좌표 계산
        x1, y1 = max(0, x - zoom_size), max(0, y - zoom_size)
        x2, y2 = min(w, x + zoom_size), min(h, y + zoom_size)
        
        # 선택 영역 추출 및 확대
        zoom_region = image[y1:y2, x1:x2]
        zoomed = cv2.resize(zoom_region, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
        
        # 원본 이미지 복사 후 확대된 영역 추가
        display = image.copy()
        zh, zw, _ = zoomed.shape
        display[10:10+zh, 10:10+zw] = zoomed  # 좌측 상단에 표시
        
        # 화면 출력
        cv2.imshow("Magnifier", display)

cv2.imshow("Magnifier", image)
cv2.setMouseCallback("Magnifier", zoom_effect)
cv2.waitKey(0)
cv2.destroyAllWindows()