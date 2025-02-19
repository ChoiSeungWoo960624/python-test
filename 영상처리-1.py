import cv2
import matplotlib.pyplot as plt

#웹캠연결
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read() # ret : True or False
#     if not ret:
#         print("프레임을 읽지 못했습니다.")
#         break # 프레임을 읽지 못하면 while문 종료
#     
#     cv2.imshow("video", frame)
#     '''
#     cv2.waitKey(1)	1ms 동안 키 입력을 기다림 (반복문에서 주로 사용)
#     cv2.waitKey(0)	무한정(Key 입력이 있을 때까지) 기다림
#     '''

#     if cv2.waitKey(1) & 0xFF == ord('q'): # q를 누르면 종료
#         #if cv2.waitkey(1) 1ms마다 키입력을 기다렸다가 q가 입력되면 종료 
#         break

# cap.release() # 영상 해제
# cv2.destroyAllWindows() # 모든 윈도우 제거


# 웹캠 열기
cap = cv2.VideoCapture(0)

# 코덱 및 비디오 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # .avi 파일 저장  / .mp4파일로 하고 싶으면 (*'mp4v')
fps = 20.0  # 초당 프레임 수

# 비디오 저장 객체 생성
out = cv2.VideoWriter("output.avi", fourcc, fps, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:
        break

    out.write(frame)  # 프레임 저장
    cv2.imshow('video', frame)  # 화면에 출력

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
        break

cap.release()
out.release()
cv2.destroyAllWindows()

