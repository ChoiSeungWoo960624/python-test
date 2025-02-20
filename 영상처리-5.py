import cv2
from ultralytics import YOLO

# model = YOLO('yolov8n.pt') # YOLO모델 V8, n:nano버전

# image = cv2.imread("test.jpg")

# #객체탐지
# results = model.predict(source=image, save=False, save_txt=False, conf=0.5)
# #source : 이미지
# #save : 결과 이미지를 저장할 것인가?
# #svae_txt : 탐지된 결과(좌표, 클래스)를 저장할것인가?
# #conf: 신뢰도 임계값. 0.5 : 50% 이상
# #반환값은 탐지 결과의 리스트형태로 나옴. results[0]이 이미지에 대한 결과

# #결과 시각화
# frame = results[0].plot()
# #plot() : 탐지된 객체를 시각화한 이미지를 반환

# cv2.imshow('YOLO', frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ==== 캠====
model = YOLO('yolov8n.pt') # YOLO모델 V8, n:nano버전
'''
# 최신버전
model = YOLO("yolo11n.pt")
'''
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("웹캠이 없습니다")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 객체탐지
    results = model.predict(source=frame, save=False, save_txt=False, conf=0.5)
    # source : 이미지
    # save : 결과 이미지를 저장할 것인가?
    # svae_txt : 탐지된 결과(좌표, 클래스)를 저장할것인가?
    # conf: 신뢰도 임계값. 0.5 : 50% 이상
    # 반환값은 탐지 결과의 리스트형태로 나옴. results[0]이 이미지에 대한 결과

    # 결과 시각화
    frame = results[0].plot()
    # plot() : 탐지된 객체를 시각화한 이미지를 반환

    cv2.imshow('YOLO', frame)

    # 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

