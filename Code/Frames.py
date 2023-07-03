import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('VideoInput/video_input2.mp4')
ret, curr_frame = cap.read()
prev_frame = curr_frame

while cap.isOpened():
    curr_frame_gr = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
    prev_frame_gr = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    
    frame_diff = cv2.absdiff(curr_frame_gr, prev_frame_gr)

    cv2.imshow('frame diff',frame_diff)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    prev_frame = curr_frame.copy()
    ret, curr_frame = cap.read()

cap.release()
cv2.destroyAllWindows()

def read_frames(cap):
    img = []

    while cap.isOpened():
        success, image = cap.read()
        if success:
            img.append(image)
        else:
            break
    cap.release()
    return print('Frames Read:',len(img))

read_frames(cap)


