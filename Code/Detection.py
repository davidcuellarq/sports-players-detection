# Import libraries needed
import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils     # Variable that gives use all about drawing utilities
mp_pose = mp.solutions.pose                 # Variable that imports the pose estimation model
pose = mp_pose.Pose()                       # Variable that access the pose estimation model
pTime = 0                                   # Establish Previous Time at 0 

cap = cv2.VideoCapture('VideoInput/video_input8.mp4')   # Setting up video capture in this case a video

while True:
    ret, frame = cap.read()                         # Reads the video and extracts the ret variable(not going to be used) and the frame variable which gives us the images of the video
    img = frame[400:1080,300:1620]                  # Reduce dimensions to focus on one tennis player only
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # MediaPipe uses Color RGB, so it's important to change from BGR to RGB
    results = pose.process(imgRGB)                  # Make detection
    if results.pose_landmarks:                      # Render detections
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
                                mp_drawing.DrawingSpec(color=(210,0,0), thickness=1, circle_radius=2),      # Specifications of the landmarks
                                mp_drawing.DrawingSpec(color=(245,60,230), thickness=2, circle_radius=2)    # Specifications of the connections
                                )

    cTime = time.time()         # Current time
    fps = 1 / (cTime - pTime)   # Variable for frames per second
    pTime = cTime               # Previous time

    cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,0), 3)      # Adds text to the video
    cv2.imshow('Video', img)                                                                # Shows the video

    if cv2.waitKey(1) & 0xFF == ord('q'):   
        break

# Function to get dimensions
# def get_dimensions(f):
#     w = f.get(cv2.CAP_PROP_FRAME_WIDTH)
#     h = f.get(cv2.CAP_PROP_FRAME_HEIGHT)
#     return w,h

# get_dimensions(cap)