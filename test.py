import pyautogui
import cv2

# force use of ImageNotFoundException
pyautogui.useImageNotFoundException()

try:
    location = pyautogui.locateOnScreen('partybutton2.png', grayscale= False, confidence=0.8 )
    print('image found')
except pyautogui.ImageNotFoundException:
    print('ImageNotFoundException: image not found')