# import d3dshot
# import time
#
# d = d3dshot.create()
# d.screenshot()
# d.screenshot_to_disk()
#
#
# time.sleep(5)
# d.stop()
# d.get_latest_frame()


# python -m pip install -U --user mss


import numpy as np
import cv2
import glob
from moviepy.editor import VideoFileClip
from mss import mss
from pil import Image
import time

color = (0, 255, 0) # bounding box color.

# This defines the area on the screen.
mon = {'top' : 10, 'left' : 10, 'width' : 1000, 'height' : 800}
sct = mss()
previous_time = 0
while True :
    sct.get_pixels(mon)
    frame = Image.frombytes( 'RGB', (sct.width, sct.height), sct.image )
    frame = np.array(frame)
    # image = image[ ::2, ::2, : ] # can be used to downgrade the input
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow ('frame', frame)
    if cv2.waitKey ( 1 ) & 0xff == ord( 'q' ) :
        cv2.destroyAllWindows()
    txt1 = 'fps: %.1f' % ( 1./( time.time() - previous_time ))
    previous_time = time.time()
    print(txt1)