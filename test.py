import pyautogui

# force use of ImageNotFoundException
pyautogui.useImageNotFoundException()

try:
    location = pyautogui.locateOnScreen('partybutton2.png', 0.5 )
    print('image found')
except pyautogui.ImageNotFoundException:
    print('ImageNotFoundException: image not found')