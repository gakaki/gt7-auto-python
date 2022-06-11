import sys
import time
import pydirectinput
import pyautogui
from airtest.core.api import *

LEFT = "left"
RIGHT = "right"
DOWN = "down"
CancelOrAccel = "esc"
Enter = "enter"

def sleep(second):
    time.sleep(0.2)

def key_down(key):
    pydirectinput.keyDown(key)


def key_up(key):
    pydirectinput.keyUp(key)


def press(key):
    # focus
    mouse_focus()
    pydirectinput.press(key)
    sleep(0.2)

def btn_cancel():
    press(CancelOrAccel)
def btn_confirm():
    press(Enter)
def left():
    press(LEFT)
def right():
    press(RIGHT)
def down():
    press(DOWN)

def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        diff = (time2 - time1)
        print('{:s} function took {:.3f} ms, '.format(
            f.__name__,  diff *1000.0))

        return ret
    return wrap

   
def l(s):
    print(f" >>> {s}")

def img_double_exists(img):
#     airtest if fails find image will usage 1 second
    if exists(img):
        return True
   
    if exists(img):
        return True
    
    return False

def wait_image(img,second=1,message_not_found="",message_ok=""):
    while img_double_exists(img) == False:
        l(message_not_found)
        sleep(second)
    l(message_ok)
    
    
def find_img(img,need_log=False):
    start = time.time()
    try:
        result = exists(img)
        if need_log == True:
            l(f"wait image {result} {time.time() - start} s")
        if result == False:
            return False
        return True
    except Exception as e:
        print(e)
    else:
        pass
    finally:
        pass


def find_ps_remote_play_window():
    return pyautogui.getWindowsWithTitle("PS Remote Play")[0]

def resize_window():
    a = find_ps_remote_play_window()

    region = [0,0,1092,717]
    a.moveTo(region[0], region[1]) # 奇怪的windows 需要-10才能靠左不然会有一条边出来
    a.resizeTo(region[2], region[3])

    mouse_focus()
    sleep(1)


def mouse_focus(need_log=False):
    a = find_ps_remote_play_window()

    ps_win_center = a.center
    if need_log == True:
        l(f"ps remote play window center : {ps_win_center}")
    pyautogui.moveTo(ps_win_center.x,ps_win_center.y)
    a.activate()
    pyautogui.click()
