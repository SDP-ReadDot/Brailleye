import pytesseract
import cv2
import numpy as np
import re
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd =  r'/usr/local/Cellar/tesseract/5.3.0_1/bin/tesseract'


img = cv2.imread('/Users/sagarikacoumarane/Desktop/SDP/Software/test_images/photoaf.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)

 
#thresholding
def thresholding(image):
    _, dst = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    return  dst
def blur(image):
    return cv2.medianBlur(image, 3)
#dilation
def dilate(image):  
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
# img = cv2.resize(img, (600, 360))




# Image rotation
# method 1
output = pytesseract.image_to_osd(img)
angle = re.search(r"Orientation in degrees: \d+", output).group().split(':')[-1].strip()
if angle == '90':
   rotated_image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
if angle == '180':
    rotated_image = cv2.rotate(img, cv2.ROTATE_180)
if angle == '270':
    rotated_image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
else:
    rotated_image = img
# cv2.imshow('Processed image', rotated_image) 

# method 2 : https://gist.github.com/scionoftech/43b4dbe9e822411787e08d59d30f5368

def check_orientation(img):
    newdata = pytesseract.image_to_osd(np.array(img))
    org_orientation = re.search('(?<=Rotate: )\d+', newdata).group(0)
    # check image orientation 
    if org_orientation != 0:
        return rotate(img)
    else:
        return img

# pip install opevcv-python==4.1.0.25 (this functionality works only in v4.1.0.25 )
def rotate(image, center=None, scale=1.0):
    angle = 360 - int(re.search('(?<=Rotate: )\d+', pytesseract.image_to_osd(image)).group(0))
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    # Perform the rotation
    mmm = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, mmm, (w, h))

    return rotated

# OUTPUT

#normalisation
norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
#rotation
img = check_orientation(img)
print(pytesseract.image_to_string(img))
cv2.imshow('Processed image', img)

cv2.waitKey(0)
