from util import *
from img import *
import random

def world_race_choose():
    
    while exists(IMG_WORLD) == False:
        l("detect IMG_WORLD found res : False")
        wait(2)
    
    down()
    wait(0.5)

    for i in range(1, 7): # awesome python can range start from 1
        right()
        wait(0.3)
    
    # confirm enter pan america
    btn_confirm()
    wait(0.1)
    btn_confirm()

    # first race loading wait
    wait(15)
    
    l("start detect IMG_START ")
    wait_image(
        IMG_CONTINUE,
        1,
        "detect IMG_CONTINUE found res : False",
        "into pan america first game race"
    )
    # continue page
    btn_confirm()
    wait(1)
    btn_confirm()

def pan_america_game():
    key_down(CancelOrAccel)
    wait(9)
    while True:
        if exists(IMG_CONTINUE_TEXT) == False:
            l(f"detect_continue_text  found res : False")

#             key_down(RIGHT)
#             wait(1)
#             key_up(RIGHT)
            times_arr = list(range(1, 10))
            times = random.choice(times_arr)
            l(f"times is {times}") 
            for i in range(1, times):
                right()

        else:
            print(f" >>> game return")
            key_up(CancelOrAccel)
            wait(1)
            return
            break
        
def pan_america_replay():
    
    l("in pan_america_replay ...")
    while exists(IMG_TO_NEXT_ROUND)== False:
        if exists(IMG_TO_NEXT_ROUND) == False:
            wait(1)
            l("not found next button")
    
    right()
    wait(0.2)
    btn_confirm()# 前往下一场比赛确定
    wait(10) # 第二场的假设loading时间
    l("out pan_america_replay")

def pan_america_next_round():
    
    while img_double_exists(IMG_CONTINUE) == False:
        l(f"detect_second_record  continue found res : False")
        wait(1)
    (f" >>> detect_second_record return")
    btn_confirm()
    wait(1)
    # 取消来到离开按钮
    btn_cancel()
    wait(0.5)

    btn_confirm()
    wait(0.2)
    btn_confirm()

    wait(20) # 回到 world race 界面

def pan_america():
    world_race_choose()
    pan_america_game()
    pan_america_dashboard()
    pan_america_replay()
    pan_america_next_round()
    pan_america()
    
# pan_america()
