import mouse
import pyautogui as py
import time
import goldenCookieClicker


def loop(delay):
    """ Sends a click with the given button and """
    x, y = py.position()
    i = 1
    while True:
        mouse.click()
        if i == 200:
            goldenCookieClicker.clickGoldenCookie()
            i = 1
        else:
            i += 1
        time.sleep(delay)
        if x != py.position()[0] or y != py.position()[1]:
            break


if __name__ == '__main__':
    print('Cookie Clicker Bot initializing em 2...\n')
    time.sleep(1)
    print('Cookie Clicker Bot initializing em 1...\n')
    time.sleep(1)
    loop(0.004)
    print('Cookie Clicker Bot ending em 1...\n')
    time.sleep(1)
