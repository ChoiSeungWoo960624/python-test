import cv2
import pytesseract

#Tesseract경로
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

image = cv2.imread('car.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 블러
blur = cv2.GaussianBlur(gray, (5, 5), 0)

#이진화
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#adaptiveThreshold : 조명에 대응 쉬운 메서드
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : 임계값 구하는 방식
#cv2.ADAPTIVE_THRESH_MEAN_C : 주변 픽셀의 평균값으로 임계값을 구함
#cv2.THRESH_BINARY : 임계값보다 크면 최대값, 작으면 0
#cv2.THRESH_BINARY_INV : 임계값보다 크면 0
#cv2.THRESH_TRUNC : 임계값보다 크면 임계값, 작으면 그대로
#cv2.THRESH_TOZERO : 임계값보다 크면 그대로, 작으면 0
#cv2.THRESH_TOZERO_INV : 임계값보다 크면 0, 작으면 그대로
#blocksize = 각픽셀의 임계값을 계산할 때 참조할 이웃영역의 크기. 반드시 흡수
#c = 평균이나 가중평균에서 차감할 값 조명에 의한 값을 세밀하게 조정

text = pytesseract.image_to_string(thresh, lang="kor", config='--psm 6')
print(text)


cv2.imshow("car", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()