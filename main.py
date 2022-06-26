from airtest.core.api import *
from airtest.cli.parser import cli_setup

import asyncio
import pyautogui


if not cli_setup():
    auto_setup(__file__, logdir=False, devices=["Windows:///?title_re=PS Remote.*"], project_root="./")

from airtest.core.settings import Settings as ST
import logging
import sys
sys.path.append(r"./")
from util import *
from race_clubman import *
from reward117 import reward117

pydirectinput.FAILSAFE = False
logging.getLogger("airtest").setLevel(logging.WARNING)

# adjust Airtest algrorism for image detect methods pirotor
# ST.CVSTRATEGY = ["mstpl","tpl", "sift","brisk"]
ST.FIND_TIMEOUT_TMP = 0.6

resize_window()

#race_clubman()
# race_x() # most like race_club_man using same script
# race_dyna()



# async def while_screen_shot():
#     while True:
#         print(datetime.now().time())
#         await screen_shoot()
#         await asyncio.sleep(1)
#         print(datetime.now().time())




# async def main():
#    results = await asyncio.gather(while_screen_shot(),reward117())
#    print(f"Results: {results}")
# asyncio.run(main())

from threading import Thread
def while_screen_shot():
    # while True:
    sleep(1)
    screen_shoot()
    while_screen_shot()

print('Main Thread: Start reward117')
thread = Thread(target=reward117)
thread.start()
thread.join()

# thread = Thread(target=race_clubman)
# thread.start()

# print('Main: Waiting for screen shot thread to terminate...')
# threadShoot = Thread(target=while_screen_shot)
# threadShoot.start()
# threadShoot.join()


# "%Y-%m-%d %H:%M:%S"  # 2022-06-25 13:11:50
# "%Y-%m-%d_%H-%M-%S"  # 2022-06-25_13_12_

