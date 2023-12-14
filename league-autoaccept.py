import pyautogui
import time

def autoclick():

    league_button_coords = None
    print("Button")

    while league_button_coords is None:
        league_button_coords = pyautogui.locateOnScreen("partybutton.jpg", 0.8)
        time.sleep(0.5)
    print("Button Found!")
    accept_center = pyautogui.center("partybutton.jpg")
    pyautogui.click(accept_center)

    time.sleep(5)
    exit()

autoclick()

