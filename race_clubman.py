from util import *
from img import *


#  just input esc to direct race until img continue image appear
def drag_race():
    l("in drag race")
    key_down(CancelOrAccel)

    sleep(8)

    for i in range(1, 5):
        right()
        sleep(0.2)

    while True:
        if img_double_exists(IMG_CONTINUE_TEXT) == False:
            l(f"detect image continue with text res : False")
            sleep(1)
        else:
            l("game break")
            key_up(CancelOrAccel)
            sleep(7)
            return


# in the game calculate score page
def calc_dashboard():
    l("in dashboard ...")
    #     because image detect need 2s if not found
    while img_double_exists(IMG_EXIT_TEXT) == False:
        l("found exit button : False")
        btn_confirm()

    l("found exit button : True")


    btn_confirm()  # press exit

    l("out dashboard")


def in_replay():
    l("in start replay")
    sleep(6)

    while exists(IMG_RETRY) == False:
        l("not found retry wait")
        sleep(1)

    l("found retry wait")
    right()
    sleep(0.2)

    btn_confirm()
    sleep(5)
    # to start page

    while exists(IMG_START) == False:
        sleep(1)

    btn_confirm()
    l("out replay")


#     return
#     while True:

#         img_replay = find_img(IMG_REPLAY)
#         img_start = find_img(IMG_START)
#         l(f"IMG_REPLAY {img_replay} , IMG_START {img_start}")

#         if img_replay == False and img_start == False:
#             btn_confirm()
#             btn_confirm()
#             l("not in replay page btn confirm twice")
#             wait(2)


#             continue

#         if img_replay == True and img_start == True:
#
#             ssbtn_confirm()
#             l("out start replay")
#             return

#         if img_replay == True and img_start == False:
#             right()
#             wait(0.2)
#             btn_confirm()
#             wait(1)
#             l("out replay page")

def race_clubman():
    drag_race()
    calc_dashboard()
    in_replay()
    race_clubman()


# race_clubman()

# almost samly process like race_clubman with race x
def race_x():
    race_clubman()


# def dyna_replay():
#     l("start replay")

#     btn_cancel()
#     sleep(0.2)
#     btn_cancel()
#     sleep(0.2)

#     # in replay choose
#     left()
#     btn_confirm()

#     while find_img(IMG_START) == False:
#         sleep(1)

#     btn_confirm()
#     sleep(2)
#     # to game run

def dyna_game():

    sleep(5)

    while True:
        if find_img(IMG_CONTINUE_TEXT,True) == False:
            l("detect_replay  found res : False")
            key_down(CancelOrAccel)
            btn_confirm()
            key_down(RIGHT)
            sleep(0.05)
            key_up(RIGHT)

            sleep(2)
        else:
            l("game break")
            key_up(RIGHT)
            key_up(CancelOrAccel)
            sleep(4)
            break


def race_dyna():
    dyna_game()
    calc_dashboard()
    in_replay()

    race_dyna()

# dyna()
# race_x()