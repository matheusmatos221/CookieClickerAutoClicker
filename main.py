import time

import mouse
import pyautogui as py

import goldenCookieClicker


def loop(delay):
    """ Sends a click with the given button and """
    x, y = py.position()
    i = 1
    while True:
        mouse.click()
        if i == 50:
            goldenCookieClicker.clickgoldencookie()
            i = 1
        else:
            i += 1
        time.sleep(delay)
        if x != py.position()[0] or y != py.position()[1]:
            break


if __name__ == '__main__':
    print('Cookie Clicker Bot initializing em 1...\n')
    time.sleep(1)
    loop(0.027)
    print('Cookie Clicker Bot ending em 1...\n')
    time.sleep(1)
