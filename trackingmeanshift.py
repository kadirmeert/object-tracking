import cv2 
import numpy as np

video = cv2.VideoCapture(r'C://mert2.mp4')

_, first_frame = video.read()
x = 250
y = 300
width = 500
height =400
roi = first_frame[y: y + height, x: x + width]  
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, roi_hist, 25, 500, cv2.NORM_MINMAX)

term_criteria = (cv2.TermCriteria_EPS  | cv2.TERM_CRITERIA_COUNT, 10, 1)
while True:
    _, frame = video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 8)

    _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)
    x, y, w, h = track_window
    cv2.rectangle(frame, (x, y), (x + w, y + h),(0, 255, 0), 2 )
    
    #cv2.imshow("Mask", mask)
    cv2.imshow("Frame",frame)

    key = cv2.waitKey(20)
    if key == 27:
        break

video.release()
video.destroyAllWindows() 