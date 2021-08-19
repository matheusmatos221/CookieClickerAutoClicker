# This script will find a Golden Cookie on Screen and click it.

import time
import pyautogui

def clickGoldenCookie():
    # Path to image to find and click on screen
    goldenCookieLocation = pyautogui.locateOnScreen('Images/GoldCookie.JPG', region=(0, 95, 970, 670), grayscale=True, confidence=0.8)

    if goldenCookieLocation != None:
        print('gold found')
        x, y = pyautogui.position()
        goldenCookiePoint = pyautogui.center(goldenCookieLocation)
        pyautogui.click(goldenCookiePoint.x, goldenCookiePoint.y)
        time.sleep(0.2)
        pyautogui.click(x, y)
        time.sleep(0.2)
    else:
        print('gold not found')
        time.sleep(0.002)

if __name__ == "__main__":
    clickGoldenCookie()