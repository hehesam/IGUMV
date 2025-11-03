import cv2
import imutils

class   manual_filter:
    def __init__(self):
        self.max_value = 255
        self.max_value_H = 360 // 2
        self.low_H = 0
        self.low_S = 0
        self.low_V = 0
        self.high_H = self.max_value_H
        self.high_S = self.max_value
        self.high_V = self.max_value
        self.window_capture_name = 'Video Capture'
        self.window_detection_name = 'Object Detection'
        self.low_H_name = 'Low H'
        self.low_S_name = 'Low S'
        self.low_V_name = 'Low V'
        self.high_H_name = 'High H'
        self.high_S_name = 'High S'
        self.high_V_name = 'High V'

        cv2.namedWindow(self.window_capture_name)
        cv2.namedWindow(self.window_detection_name)
        cv2.createTrackbar(self.low_H_name, self.window_detection_name, self.low_H, self.max_value_H, self.on_low_H_thresh_trackbar)
        cv2.createTrackbar(self.high_H_name, self.window_detection_name, self.high_H, self.max_value_H, self.on_high_H_thresh_trackbar)
        cv2.createTrackbar(self.low_S_name, self.window_detection_name, self.low_S, self.max_value, self.on_low_S_thresh_trackbar)
        cv2.createTrackbar(self.high_S_name, self.window_detection_name, self.high_S, self.max_value, self.on_high_S_thresh_trackbar)
        cv2.createTrackbar(self.low_V_name, self.window_detection_name, self.low_V, self.max_value, self.on_low_V_thresh_trackbar)
        cv2.createTrackbar(self.high_V_name, self.window_detection_name, self.high_V, self.max_value, self.on_high_V_thresh_trackbar)

    def on_low_H_thresh_trackbar(self,val):

        low_H = val
        low_H = min(self.high_H - 1, low_H)
        cv2.setTrackbarPos(self.low_H_name, self.window_detection_name, low_H)


    def on_high_H_thresh_trackbar(self,val):

        high_H = val
        high_H = max(high_H, self.low_H + 1)
        cv2.setTrackbarPos(self.high_H_name, self.window_detection_name, high_H)


    def on_low_S_thresh_trackbar(self,val):

        low_S = val
        low_S = min(self.high_S - 1, low_S)
        cv2.setTrackbarPos(self.low_S_name, self.window_detection_name, low_S)


    def on_high_S_thresh_trackbar(self,val):
        high_S = val
        high_S = max(high_S, self.low_S + 1)
        cv2.setTrackbarPos(self.high_S_name, self.window_detection_name, high_S)


    def on_low_V_thresh_trackbar(self,val):
        low_V = val
        low_V = min(self.high_V - 1, low_V)
        cv2.setTrackbarPos(self.low_V_name, self.window_detection_name, low_V)


    def on_high_V_thresh_trackbar(self,val):
        high_V = val
        high_V = max(high_V, self.low_V + 1)
        cv2.setTrackbarPos(self.high_V_name, self.window_detection_name, high_V)


class   ball_detection:
    def __init__(self):

        self.all_centers = []
        self.point_list = []
        self.max_value = 255
        self.max_value_H = 360 // 2
        self.low_H = 0
        self.low_S = 0
        self.low_V = 0
        self.high_H = self.max_value_H
        self.high_S = self.max_value
        self.high_V = self.max_value
        self.window_capture_name = 'Video Capture'
        self.window_detection_name = 'Object Detection'
        self.low_H_name = 'Low H'
        self.low_S_name = 'Low S'
        self.low_V_name = 'Low V'
        self.high_H_name = 'High H'
        self.high_S_name = 'High S'
        self.high_V_name = 'High V'

        cv2.namedWindow(self.window_capture_name)
        cv2.namedWindow(self.window_detection_name)
        cv2.createTrackbar(self.low_H_name, self.window_detection_name, self.low_H, self.max_value_H, self.on_low_H_thresh_trackbar)
        cv2.createTrackbar(self.high_H_name, self.window_detection_name, self.high_H, self.max_value_H, self.on_high_H_thresh_trackbar)
        cv2.createTrackbar(self.low_S_name, self.window_detection_name, self.low_S, self.max_value, self.on_low_S_thresh_trackbar)
        cv2.createTrackbar(self.high_S_name, self.window_detection_name, self.high_S, self.max_value, self.on_high_S_thresh_trackbar)
        cv2.createTrackbar(self.low_V_name, self.window_detection_name, self.low_V, self.max_value, self.on_low_V_thresh_trackbar)
        cv2.createTrackbar(self.high_V_name, self.window_detection_name, self.high_V, self.max_value, self.on_high_V_thresh_trackbar)

        
    def start(self):

        phase = 0
        frame_index = 0

        cap = cv2.VideoCapture(0)
        # mf = manual_filter()
        while True:
            frame_index += 1

            print(f"frame: {frame_index}")
            _, frame = cap.read()

            if frame is None :
                break

            if phase == 0 :
                print(self.window_capture_name)
                frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                frame_threshold = cv2.inRange(frame_HSV, (self.low_H, self.low_S, self.low_V), (self.high_H, self.high_S, self.high_V))
                cv2.imshow(self.window_capture_name, frame)
                cv2.imshow(self.window_detection_name, frame_threshold)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
    def on_low_H_thresh_trackbar(self,val):
        low_H = self.low_H
        high_H = self.high_H
        low_H = val
        low_H = min(high_H - 1, low_H)
        print(self.low_H_name)
        cv2.setTrackbarPos(self.low_H_name, self.window_detection_name, low_H)


    def on_high_H_thresh_trackbar(self,val):

        high_H = val
        high_H = max(high_H, self.low_H + 1)
        cv2.setTrackbarPos(self.high_H_name, self.window_detection_name, high_H)


    def on_low_S_thresh_trackbar(self,val):

        low_S = val
        low_S = min(self.high_S - 1, low_S)
        cv2.setTrackbarPos(self.low_S_name, self.window_detection_name, low_S)


    def on_high_S_thresh_trackbar(self,val):
        high_S = val
        high_S = max(high_S, self.low_S + 1)
        cv2.setTrackbarPos(self.high_S_name, self.window_detection_name, high_S)


    def on_low_V_thresh_trackbar(self,val):
        low_V = val
        low_V = min(self.high_V - 1, low_V)
        cv2.setTrackbarPos(self.low_V_name, self.window_detection_name, low_V)


    def on_high_V_thresh_trackbar(self,val):
        high_V = val
        high_V = max(high_V, self.low_V + 1)
        cv2.setTrackbarPos(self.high_V_name, self.window_detection_name, high_V)

bd = ball_detection()
bd.start()