import glob
from PIL import Image
import RPi.GPIO as GPIO
import cv2
import time
import sys
import os

import capture
import gifmaster


#button
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#shot
GPIO.add_event_detect(my_input, GPIO.FALLING, callback=cap())

#create gif
imgin = "/home/pi/*.jpg"
imgout = "/home/pi/image.gif"
gifmaster(imgin,imgout)