import cv2
import numpy as np
import dlib

video = cv2.VideoCapture(r'C://mert.mp4')


if video.isOpened() == False:
    print('video cannot be opened successfully')


