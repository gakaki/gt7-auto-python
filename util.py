import sys
import time
import pydirectinput
import pyautogui


from airtest.core.api import *
from datetime import datetime
LEFT = "left"
RIGHT = "right"
UP = "up"
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
def up():
    press(DOWN)
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

region = [0,0,1788,1109]

def resize_window():
    global region
    a = find_ps_remote_play_window()
    l(a.size)

    a.moveTo(region[0], region[1]) # 奇怪的windows 需要-10才能靠左不然会有一条边出来
    a.resizeTo(region[2], region[3])

    mouse_focus()
    sleep(1)

def get_screen_shot_name():
    now = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    # print("ScreenShot at ", now)
    return f'./screenshot/{now}.png'

# 检测黑边
# 检测截取范围

def screen_shoot():
    global  region
    new_region= [98,120,1587,891]
    screenshot = pyautogui.screenshot(region=new_region)
    file_name = get_screen_shot_name()
    screenshot.save(file_name)
    return file_name

def mouse_focus(need_log=False):
    a = find_ps_remote_play_window()

    ps_win_center = a.center
    if need_log == True:
        l(f"ps remote play window center : {ps_win_center}")
    pyautogui.moveTo(ps_win_center.x,ps_win_center.y)
    a.activate()
    pyautogui.click()


def all_pixel_match(pos_and_pixels = [],falls_call_back_func=None):
    try:
        start = time.time()
        if len(pos_and_pixels) <= 0:
            l(f"not get  PIXEL pos_and_pixels")
            return False

        boolean_expressions = [pyautogui.pixelMatchesColor(row[0],row[1],row[2],tolerance=10)  for row in pos_and_pixels]
        result = all(boolean_expressions)
        l(f"detect PIXEL found res : {result}, {time.time() - start} s,{boolean_expressions}")
        if result == False:
            if falls_call_back_func != None:
                falls_call_back_func()
            all_pixel_match(pos_and_pixels,falls_call_back_func)
        else:
            return True

    except Exception as e:
        print(e)
        all_pixel_match(pos_and_pixels,falls_call_back_func)

