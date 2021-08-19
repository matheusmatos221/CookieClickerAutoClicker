# This script will find a Golden Cookie on Screen and click it.

import time
import pyautogui

def clickGoldenCookie()
    # Delay between searches in seconds
    delay = 2
    while True:
        # Path to image to find and click on screen
        goldenCookieLocation = pyautogui.locateOnScreen('Images/GoldCookie.JPG', region=(0, 95, 970, 670), grayscale=True, confidence=0.8)

        if goldenCookieLocation != None:
            goldenCookiePoint = pyautogui.center(goldenCookieLocation)
            pyautogui.click(goldenCookiePoint.x, goldenCookiePoint.y)
            time.sleep(delay)
        else:
            time.sleep(delay)

if __name__ == "__main__":
    clickGoldenCookie()