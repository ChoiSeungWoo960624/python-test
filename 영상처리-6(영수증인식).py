import cv2
import pytesseract

#Tesseract경로
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

image = cv2.imread("receipt.png")

#흑백변환환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# tesseract를 이용해서 이미지에서 텍스트를 추출
text = pytesseract.image_to_string(gray, lang="kor+eng")

print("추출된 텍스트 : ", text)