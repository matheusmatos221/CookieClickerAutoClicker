# This script will find a Golden Cookie on Screen and click it.

import time
import pyautogui


def clickgoldencookie():
    # Path to image to find and click on screen
    golden_cookie_location = pyautogui.locateOnScreen('Images/GoldCookie.JPG', region=(0, 95, 970, 670), grayscale=True,
                                                      confidence=0.8)

    if golden_cookie_location is not None:
        print('gold found')
        x, y = pyautogui.position()
        golden_cookie_point = pyautogui.center(golden_cookie_location)
        pyautogui.click(golden_cookie_point.x, golden_cookie_point.y)
        time.sleep(0.2)
        pyautogui.click(x, y)
        time.sleep(0.2)
    else:
        print('gold not found')
        time.sleep(0.002)


def main_loop(delay):
    """ Sends a click with the given button and """
    x, y = pyautogui.position()
    while True:
        clickgoldencookie()
        time.sleep(delay)
        if x != pyautogui.position()[0] or y != pyautogui.position()[1]:
            break


if __name__ == "__main__":
    print('Cookie Clicker Bot initializing em 1...\n')
    time.sleep(1)
    main_loop(0.027)
