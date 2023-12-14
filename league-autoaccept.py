import pyautogui
import time
import cv2


def autoclick():

    league_button_coords = None
    print("Button")
    pyautogui.useImageNotFoundException()
    while league_button_coords is None:
        league_button_coords = pyautogui.locateOnScreen("partybutton.png", grayscale=False, confidence=0.7)
        time.sleep(0.5)
    print("Button Found!")
    accept_center = pyautogui.center(league_button_coords)
    print(accept_center)
    pyautogui.click(accept_center)

    time.sleep(5)
    exit()

autoclick()

