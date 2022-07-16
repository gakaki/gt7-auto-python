from airtest.core.api import *
from airtest.cli.parser import cli_setup
from threading import Thread
import asyncio # asyncio not usage
import pyautogui
import logging
import sys
sys.path.append(r"./")
from util import *
from race_clubman import *
from reward117 import reward117


# airtest setup
if not cli_setup():
    auto_setup(__file__, logdir=False, devices=["Windows:///?title_re=PS Remote.*"], project_root="./")
from airtest.core.settings import Settings as ST
logging.getLogger("airtest").setLevel(logging.WARNING)
# adjust Airtest algrorism for image detect methods pirotor
# ST.CVSTRATEGY = ["mstpl","tpl", "sift","brisk"]
ST.FIND_TIMEOUT_TMP = 0.6 # image search find timeout 0.6s


pydirectinput.FAILSAFE = False

resize_window()

print('Main Thread: Start race_clubman')
# just change reward117 with 'race_clubman' or race_x or race_dyna or race_pan_america
thread = Thread(target=race_clubman)
# thread = Thread(target=race_clubman)
# thread = Thread(target=race_x())
# thread = Thread(target=race_dyna)
# thread = Thread(target=race_pan_america)
thread.start()
thread.join()

# start screen shot every 1s
def start_screen_shot():
    print('Main: Waiting for screen shot thread to terminate...')
    def while_screen_shot():
        # while True:
        sleep(1)
        screen_shoot()
        while_screen_shot()
    threadShoot = Thread(target=while_screen_shot)
    threadShoot.start()
    threadShoot.join()

# not know why asyncio is error 
# async def main():
#    results = await asyncio.gather(while_screen_shot(),reward117())
#    print(f"Results: {results}")
# asyncio.run(main())
