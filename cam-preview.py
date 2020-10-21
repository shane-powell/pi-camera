from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 90
camera.start_preview(fullscreen=False,window=(490,0,300,480), rotation=90)
#camera.start_preview()
sleep(7)
camera.stop_preview()
