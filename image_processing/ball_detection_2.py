import cv2
import imutils
import time
import math
import multiple_frames
from pygame import mixer




def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H - 1, low_H)
    cv2.setTrackbarPos(low_H_name, window_detection_name, low_H)


def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H + 1)
    cv2.setTrackbarPos(high_H_name, window_detection_name, high_H)


def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S - 1, low_S)
    cv2.setTrackbarPos(low_S_name, window_detection_name, low_S)


def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S + 1)
    cv2.setTrackbarPos(high_S_name, window_detection_name, high_S)


def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V - 1, low_V)
    cv2.setTrackbarPos(low_V_name, window_detection_name, low_V)


def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V + 1)
    cv2.setTrackbarPos(high_V_name, window_detection_name, high_V)

def gradient(pt1, pt2):
    if pt2[0]-pt1[0] == 0 :
        return (pt2[1]-pt1[1])/(pt2[0]-pt1[0] + 1)
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])



def getAngle(all_centers,frame, index, frame_height, hit_state):
    pt1, pt2, pt3 = all_centers[-3:]

    m1 = gradient(pt2, pt1)
    m2 = gradient(pt2, pt3)
    if 1+(m2*m1) == 0 :
        m1 += 1
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
    cv2.putText(frame,str(angD), (pt1[0]-40, pt1[1]-20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,255, 2))


    # time.sleep(0.5)

    if abs(angD) > 17 and not hit_state:
        hit_state = True
        cv2.putText(frame, "wall hit", (pt1[0] - 40, pt1[1] - 50), cv2.FACE_RECOGNIZER_SF_FR_COSINE, 1.5, (255, 0, 255, 2))
        mixer.init()
        sound = mixer.Sound("hit1.wav")
        sound.play()
        cv2.imwrite("pics/frame"+str(index)+".png", cv2.resize(frame, (int(height / 2), int(width / 2))))
        data = (pt2[0],frame_height-pt2[1])
        print("index 0",data[0], "index 1", data[1])


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        point_list.append([x,y])



max_value = 255
max_value_H = 360 // 2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'

cv2.namedWindow(window_capture_name)
cv2.namedWindow(window_detection_name)
cv2.createTrackbar(low_H_name, window_detection_name, low_H, max_value_H, on_low_H_thresh_trackbar)
cv2.createTrackbar(high_H_name, window_detection_name, high_H, max_value_H, on_high_H_thresh_trackbar)
cv2.createTrackbar(low_S_name, window_detection_name, low_S, max_value, on_low_S_thresh_trackbar)
cv2.createTrackbar(high_S_name, window_detection_name, high_S, max_value, on_high_S_thresh_trackbar)
cv2.createTrackbar(low_V_name, window_detection_name, low_V, max_value, on_low_V_thresh_trackbar)
cv2.createTrackbar(high_V_name, window_detection_name, high_V, max_value, on_high_V_thresh_trackbar)

greenLower = (46, 65, 50)
greenUpper = (80, 255, 255)



vs = cv2.VideoCapture(0)
all_centers = [] # cordinates of ball in each frame
point_list = [] # clicked postion
hit_state = False # when ball hit the wall 
phase = 0
i = 0

ball_detected = False
load = 0
load = int(input("load parameters: "))

while True:
    i += 1
    print("frame : ",i)
    _, frame = vs.read()

    if frame is None:
        break
    

    if load == 1:
        cv2.destroyAllWindows()
        file = open("threshold.txt", 'r')
        res = file.read()
        print(res)
        arr = res.split(" ")
        greenLower = (int(arr[0]),int(arr[1]),int(arr[2]))
        greenUpper = (int(arr[3]),int(arr[4]),int(arr[5]))
        print(greenLower, greenUpper)
        phase = 1
        load = 0

    if phase == 0:
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_threshold = cv2.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
        cv2.imshow(window_capture_name, frame)
        cv2.imshow(window_detection_name, frame_threshold)
        cv2.setMouseCallback(window_capture_name, mousePoints)

        if len(point_list) == 2 :
            cv2.destroyAllWindows()
            greenLower = (low_H, low_S, low_V)
            greenUpper = (high_H, high_S, high_V)
            file = open("threshold.txt", 'w')
            res = f"{low_H} {low_S} {low_V} {high_H} {high_S} {high_V}"
            file.write(res)
            file.close()

            phase = 1
            point_list.clear()

    if phase == 1:
        for x,y in point_list:
            cv2.circle(frame, (x, y), 5, (0, 255, 255), cv2.FILLED)
        cv2.imshow("frame", frame)
        cv2.setMouseCallback("frame", mousePoints)
        if len(point_list) == 2:
            x1, y1 = point_list[0]
            x2, y2 = point_list[1]
            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255), 4)
            phase = 2
            cv2.destroyAllWindows()
            i = 0

    elif phase == 2:
        x1, y1 = point_list[0]
        x2, y2 = point_list[1]
        frame = frame[y1:y2, x1:x2]
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)

        height , width = frame.shape[:2]

        print("w & h", width, height)

        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        mask1 = cv2.inRange(hsv, greenLower, greenUpper)

        mask2 = cv2.erode(mask1, None, iterations=4)

        mask3 = cv2.dilate(mask2, None, iterations=6)

        #  finding contours is like finding white object from black background.

        cnts = cv2.findContours(mask3.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts) # returns center
        center = None
        # print(cnts)
        if len(cnts) > 0:
            ball_detected = True
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            # To see the centroid clearly
            print("R : ",radius)
            if radius > 1 and radius < 500:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 5)
                all_centers.append(center)
                for ii in all_centers:
                    cv2.circle(frame, ii, 5, (0, 0, 255), -1)
                if len(all_centers) >= 3:
                    getAngle(all_centers, frame, i, height, hit_state)

        elif ball_detected == True :
            ball_detected = False
            hit_state = False
            all_centers.clear()

        imgStack = multiple_frames.stackImages(0.8, ([frame, mask1], [mask2, mask3]))
        cv2.imshow("Frame", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('c'):
        point_list.clear()

vs.release()
cv2.destroyAllWindows()