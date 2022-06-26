from race_clubman import calc_dashboard
from util import *
from img import *
import random
import pyautogui

def wait_cafe_menu():
    try:
        if exists(IMG_CAFE) == False:
            l("detect IMG_CAFE found res : False")
            sleep(0.5)
            wait_cafe_menu()
        l("detect IMG_CAFE found res : True")
    except Exception as e:
        print(e)
        wait_cafe_menu()

def wait_car_home():
    try:
        if exists(IMG_CAR_HOME) == False:
            l("detect IMG_CAR_HOME found res : False")
            sleep(0.5)
            wait_car_home()
        l("detect IMG_CAR_HOME found res : True")
    except Exception as e:
        print(e)
        wait_car_home()

def wait_already_get_reward():
    try:
        if exists(IMG_RECEIVED) == False:
            l("detect IMG_ALREADY_GOT found res : False")
            btn_confirm()
            sleep(0.5)
            wait_already_get_reward()

        l("detect IMG_ALREADY_GOT found res : True")

    except Exception as e:
        print(e)
        wait_already_get_reward()



def wait_already_get_reward_pixel():
    pos_and_pixels = [
         [397, 363, (178, 178, 178)],
         [412, 362, (161, 161, 161)]
    ]
    def call_back():
        l("detect IMG_ALREADY_GOT found res : False")
        btn_confirm()
        sleep(0.5)
    if all_pixel_match(pos_and_pixels,call_back) == True:
        l("detect IMG_ALREADY_GOT found res : True")
        sleep(0.5)
        return True
    else:
        return False

def wait_cafe_menu_pixel():
    pos_and_pixels = [
     [886, 545, (253, 253, 255)],
     [903, 545, (254, 254, 254)]
    ]

    def call_back():
        l("detect PIXEL_CAFE found res : False")
        sleep(0.5)
    if all_pixel_match(pos_and_pixels,call_back) == True:
        l("detect PIXEL_CAFE found res : True")
        sleep(1)
        return True
    else:
        return False

def reward(is_want_engine=False):

    btn_confirm()
    sleep(3.5)

    # 奖杯
    left()

    # 我的收藏
    btn_confirm()

    down()

    right()

    btn_confirm()

    # append menu page
    up()

    # rotate engine
    if is_want_engine == True:
        right()
        right()
    else:# toyota 86
        pass

    btn_confirm()
    sleep(0.5)
    btn_confirm()
    sleep(0.7)

    btn_cancel()
    btn_cancel()
    btn_cancel()

    # loading time for return to dashboard
    sleep(5)

def to_garage():
    wait_cafe_menu_pixel()

    right()
    btn_confirm()
    # loading into  car home
    sleep(7.5)

    right()
    right()
    right()

    #into get reward page
    btn_confirm()
    sleep(0.5)
    btn_confirm()
    btn_confirm()

    # wait the reward animation
    sleep(11)
    wait_already_get_reward_pixel()

    btn_cancel()
    btn_cancel()

    sleep(4)

    wait_car_home()

    left()

def reward117():

    start = time.time()

    reward(False)
    to_garage()

    reward(True)
    to_garage()

    l(f"reward117 usage {time.time() - start} s")

    reward117()

