import pytesseract
import cv2
import numpy as np
import re
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd =  r'/usr/local/Cellar/tesseract/5.3.0_1/bin/tesseract'


img = cv2.imread('.jpg')#insert img pathh here

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Orientation check

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
#greyscale
img = get_grayscale(img)
#rotation
img = check_orientation(img)
print(pytesseract.image_to_string(img))
cv2.imshow('Processed image', img)

cv2.waitKey(0)
