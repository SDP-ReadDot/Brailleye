import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'


def main(filepath):
    img = cv2.imread(filepath)
    # img = cv2.resize(img, (600, 360))
    print(pytesseract.image_to_string(img))
    # cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == "__main__":
    filePath = 'images/sample3.jpg'
    main(filePath)
