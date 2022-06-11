from airtest.core.api import *

IMG_DIR    = "images/en/"
IMG_DIR    = "images/cn/"

def get_img_path(name):
    return f"{IMG_DIR}{name}"
 
    
    

IMG_REPLAY = Template(get_img_path("tpl1654767689921.png"), threshold=0.9000000000000001, record_pos=(-0.075, 0.214), resolution=(1884, 1093))

IMG_WORLD  = Template(get_img_path("tpl1654767832175.png"), record_pos=(-0.001, 0.167), resolution=(1884, 1093))


IMG_START  = Template(get_img_path("tpl1654767740147.png"), record_pos=(-0.217, 0.213), resolution=(1884, 1093))


IMG_TO_NEXT_ROUND = Template(get_img_path("tpl1654770464330.png"), threshold=0.8, target_pos=5, record_pos=(0.056, 0.213), resolution=(1188, 802))

IMG_CONTINUE = Template(get_img_path("tpl1654770600090.png"), threshold=0.8, record_pos=(-0.013, 0.222), resolution=(1188, 802))

IMG_CONTINUE_TEXT = Template(get_img_path("tpl1654915236604.png"), threshold=0.8
                             ,  record_pos=(0.003, 0.234), resolution=(1076, 678))

IMG_EXIT_TEXT = Template(get_img_path("tpl1654774813209.png"), record_pos=(0.399, 0.211), resolution=(1076, 678))

IMG_RETRY = Template(get_img_path("tpl1654771787714.png"), threshold=0.8500000000000001, target_pos=4, record_pos=(-0.007, 0.213), resolution=(1076, 678))





