import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

imPath = 'sample-4.jpg'
im = cv2.imread(str(imPath), cv2.IMREAD_COLOR)

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

new_data = pytesseract.image_to_osd(im)
gray_data = pytesseract.image_to_osd(gray)
print(new_data)
print(gray_data)

print(pytesseract.image_to_string(im))
# re.search('(?<=Rotate: )\d+', new_data).group(0)

def rotate(image, center=None, scale=1.0):
    angle = 360 - int(re.search('(?<=Rotate: )\d+', pytesseract.image_to_osd(image)).group(0))
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    # Perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated


f = rotate(gray)

cv2.imshow('lol', f)

print(pytesseract.image_to_string(f))
# print(pytesseract.image_to_string(gray))

# rotate(im)
