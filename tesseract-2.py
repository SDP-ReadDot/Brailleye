import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('sample3.jpg')

# img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_string(img))
# cv2.imshow('Result', img)
cv2.waitKey(0)
