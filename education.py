import pygame
import keyboard
import time

pygame.init()
pygame.mixer.init()

baseDir = '/Users/punch/Brailleye/educationsounds/'
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#Given index of the letter, play the sound for that letter and output on display
def playLetter(indexOfLetter):
    letterDir = baseDir + letters[indexOfLetter] + ".mp3"
    sound = pygame.mixer.Sound(letterDir)
    #Substiute for output on diplay
    print(letters[indexOfLetter])
    playing = sound.play()
    while playing.get_busy():
        pygame.time.delay(50)
    if keyboard.read_key() == "d":
        if  indexOfLetter + 1 < len(letters):
            playLetter(indexOfLetter + 1)
        else:
            playLetter(indexOfLetter)
    elif keyboard.read_key() == "a":
        if indexOfLetter > 0:
            playLetter(indexOfLetter - 1)
        else:
            playLetter(indexOfLetter)
    elif keyboard.read_key() == "esc":
        pass
    
if __name__ == "__main__":
    playLetter(0)