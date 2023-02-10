import cv2
# Import all neccessary features to code.
import RPi.GPIO as GPIO

from time import sleep

# If code is stopped while the solenoid is active it stays active
# This may produce a warning if the code is restarted and it finds the GPIO Pin, which it defines as non-active in next line, is still active
# from previous time the code was run. This line prevents that warning syntax popping up which if it did would stop the code running.
GPIO.setwarnings(False)
# This means we will refer to the GPIO pins
# by the number directly after the word GPIO. A good Pin Out Resource can be found here https://pinout.xyz/
GPIO.setmode(GPIO.BCM)
# This sets up the GPIO 18 pin as an output pin
GPIO.setup(17, GPIO.OUT)  # 1
GPIO.setup(18, GPIO.OUT)  # 2
GPIO.setup(27, GPIO.OUT)  # 3
GPIO.setup(22, GPIO.OUT)  # 4
GPIO.setup(23, GPIO.OUT)  # 5
GPIO.setup(24, GPIO.OUT)  # 6

code_table = {
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
    '#': '001111',
    '1': '100000',
    '2': '110000',
    '3': '100100',
    '4': '100110',
    '5': '100010',
    '6': '110100',
    '7': '110110',
    '8': '110010',
    '9': '010100',
    '0': '010110',
    ' ': '000000'}


def promptInput():
    text = input("Please input a text: ")
    return text


def charToBraille(char):
    if (char.isalpha()):
        char = char.lower()
    return code_table[char]


# 1st dot
# while (True):
def first_dot():
    # #This Turns Relay Off. Brings Voltage to Max GPIO can output ~3.3V
    #     while ()
    GPIO.output(17, 1)
    # Wait 1 Seconds
    sleep(1)
    # Turns Relay On. Brings Voltage to Min GPIO can output ~0V.
    GPIO.output(17, 0)
    # Wait 1 Seconds
    sleep(1)


def controller(braille_bin):
    print(braille_bin[0])
    if braille_bin[0] == '1':
        print(braille_bin[0])
        GPIO.output(17, 1)
        # first_dot()


if __name__ == '__main__':
    t = promptInput()
    print(t)
    br = charToBraille(t)
    print(br)
    controller(br)
    sleep(5)

print("hello")