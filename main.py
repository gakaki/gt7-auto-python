from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=False, devices=["Windows:///?title_re=PS Remote.*"], project_root="C:/Users/g/Desktop/work/jwt/gt7_airtest")

from airtest.core.settings import Settings as ST
import logging
import sys
sys.path.append(r"./")
from util import *
from race_clubman import *

pydirectinput.FAILSAFE = False
logging.getLogger("airtest").setLevel(logging.WARNING)

# # 调整Airtest图像识别算法的使用顺序
# ST.CVSTRATEGY = ["mstpl","tpl", "sift","brisk"]
ST.FIND_TIMEOUT_TMP = 0.5

resize_window()

race_clubman()
# race_x() # most like race_club_man using same script
# race_dyna()








