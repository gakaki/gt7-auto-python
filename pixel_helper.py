import pyautogui
from pynput import mouse, keyboard
from threading import main_thread, Thread
from util import l
import time

def get_current_mouse_pos_and_rgb():
    x, y = pyautogui.position()
    im = pyautogui.screenshot()
    current = [x,y,im.getpixel((x, y))]
    l(f'current mouse position and rgb {current}')
    return current

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    get_current_mouse_pos_and_rgb()
    # if not pressed:
    #     # Stop listener
    #     return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        # on_move=on_move,
        on_click=on_click,
        # on_scroll=on_scroll
) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    # on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll
)
listener.start()



def detect_mouse_rgb_position():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)

            get_current_mouse_pos_and_rgb()
            time.sleep(2)

    except KeyboardInterrupt:
        print('\n')


l('helper: Waiting for detect mouse position and pixel...')
threadMouse = Thread(target=detect_mouse_rgb_position)
threadMouse.start()
threadMouse.join()
