import mouse
import pyautogui as py
import time
import goldenCookieClicker


def loop(delay):
    """ Sends a click with the given button and """
    x, y = py.position()
    while True:
        mouse.click()
        goldenCookieClicker.clickGoldenCookie()
        time.sleep(delay)
        if x != py.position()[0] or y != py.position()[1]:
            break


if __name__ == '__main__':
    print('Cookie Clicker Bot initializing em 1...\n')
    time.sleep(1)
    loop(0.002)
    print('Cookie Clicker Bot ending em 1...\n')
    time.sleep(1)