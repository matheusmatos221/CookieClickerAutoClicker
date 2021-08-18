import mouse,keyboard, time, pyautogui as py

def loop(delay):
    """ Sends a click with the given button and """
    x, y = py.position()
    while True:
        mouse.click()
        time.sleep(delay)
        if x != py.position()[0] or y != py.position()[1]:
            break


if __name__ == '__main__':
    print('Cookie Clicker Bot inicializando em 3...\n')
    time.sleep(1)
    print('Cookie Clicker Bot inicializando em 2...\n')
    time.sleep(1)
    print('Cookie Clicker Bot inicializando em 1...\n')
    time.sleep(1)
    loop(0.1)