import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('images/sample3.jpg')


print(pytesseract.image_to_string(img))

cv2.waitKey(0)
