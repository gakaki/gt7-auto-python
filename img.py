from airtest.core.api import *

def get_img_path(name):
    img_name = f"./images/{name}"
    print(img_name)
    return img_name

IMG_REPLAY = Template(get_img_path("replay.png"), threshold=0.9000000000000001, record_pos=(-0.075, 0.214), resolution=(1884, 1093))

IMG_WORLD  = Template(get_img_path("world_race.png"), record_pos=(-0.001, 0.167), resolution=(1884, 1093))


IMG_START  = Template(get_img_path("start.png"), record_pos=(-0.217, 0.213), resolution=(1884, 1093))


IMG_TO_NEXT_ROUND = Template(get_img_path("to_next_race.png"), threshold=0.8, target_pos=5, record_pos=(0.056, 0.213), resolution=(1188, 802))


IMG_CONTINUE_TEXT = Template(get_img_path("continue_txt.png"),   threshold=0.9,  record_pos=(0.001, 0.22), resolution=(2201, 1172))

IMG_EXIT_TEXT = Template(get_img_path("exit.png"), record_pos=(0.399, 0.211), resolution=(1076, 678))

IMG_RETRY = Template(get_img_path("retry.png"), threshold=0.8500000000000001, target_pos=4, record_pos=(-0.007, 0.213), resolution=(1076, 678))

IMG_CONTINUE = Template(get_img_path("icon_continue.png"), threshold=0.8, record_pos=(-0.013, 0.222), resolution=(1188, 802))

IMG_RECEIVED = Template(get_img_path(r"received_cn.png"), record_pos=(-0.281, -0.111), resolution=(1772, 1070))

IMG_CAFE = Template(get_img_path(r"cafe.png"), record_pos=(-0.007, -0.011), resolution=(1772, 1070))
IMG_CAR_HOME = Template(get_img_path(r"car_home.png"), record_pos=(0.159, 0.003), resolution=(1259, 716))







