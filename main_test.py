import mouse,keyboard, time

def loop(delay):
    """ Sends a click with the given button and """

    print("Press Ctrl-C to terminate while statement")
    while True:
        mouse.click()
        time.sleep(delay)

        if keyboard.is_pressed(ctrl):
            print(keyboard.is_pressed(ctrl))
            break


if __name__ == '__main__':
    print('Cookie Clicker Bot inicializando em 3...\n')
    time.sleep(1)
    print('Cookie Clicker Bot inicializando em 2...\n')
    time.sleep(1)
    print('Cookie Clicker Bot inicializando em 1...\n')
    time.sleep(1)
    loop(1)