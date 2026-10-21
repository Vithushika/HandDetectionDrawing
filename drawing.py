#pip install opencv-python
#pip install mediapipe

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import random 

base_options = python.BaseOptions(model_asset_path='hand_landmarker.task') #loads pretrained handtracking model
options = vision.HandLandmarkerOptions(base_options=base_options,num_hands=1) #configurations for the model + how many hands to detect
detector = vision.HandLandmarker.create_from_options(options) #initialize hand detector using the configurations

cap = cv2.VideoCapture(0)
draw = False
drawings = []
size = 5
colour = (255,255,255)
connections = [(0,1), (1,2), (2,3), (3,4), #thumb
               (1,5), (5,6), (6,7), (7,8), #index
               (5,9), (9,10), (10,11), (11,12), #middle
               (9,13), (13,14), (14,15), (15,16), #ring
               (13,17), (17,18), (18,19), (19,20), #pinky
               (0,17) #wrist to pinky
]

while True:
    ref, frame = cap.read()
    if ref == False:
        continue

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    rbgFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mpimage = mp.Image(image_format=mp.ImageFormat.SRGB, data=rbgFrame) #convert open cv image to mp image
    recognizer_result = detector.detect(mpimage) #take each frame and recognize gestures
    
    key = cv2.waitKey(1) & 0xFF #every milisec look for key presses, convert it to ASCII 
    if key == 27: #esc key
        break
    if key == ord(' '):
        cv2.waitKey(5)  
        draw = not draw
    if key == ord('c'):
        drawings = []
        cv2.waitKey(5) 

    if key == ord('='): #add size
        size += 1
        cv2.waitKey(5) 
    if key == ord('-') and size > 1: #minus size
        size -= 1
        cv2.waitKey(5)
    if key == ord('w'):
        colour = (255,255,255)
        cv2.waitKey(5)
    if key == ord('r'):
        colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        cv2.waitKey(5)
        
    cv2.putText(frame, f"Drawing: {draw}", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)
    cv2.putText(frame, f"Size: {size}", (5, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)

    for point,brushsize,brushcolour in drawings:
            cv2.circle(frame, point, brushsize, brushcolour, -1)

    if recognizer_result.hand_landmarks: #if any hand is recognized...
        hand_landmarks = recognizer_result.hand_landmarks #grab handlandmarks
        indexFinger = hand_landmarks[0][8]
        points = []
        for lm in hand_landmarks[0]: #for each landmark detected on hand 
            #draw landmarks
            x, y = int(lm.x * w), int(lm.y * h)
            ix,iy = int(indexFinger.x * w), int(indexFinger.y * h)
            points.append((x,y))
            #cv2.circle(frame, (x, y), 5, (255,255,255), -1)
            cv2.circle(frame, (ix, iy), size+1, (0,0,0), -1)
            cv2.circle(frame, (ix, iy), size, colour, -1)
            
        #draw connections
        #if len(points) == 21:
        for start, end in connections:
            cv2.line(frame, points[start], points[end], (0,0,0), 2)
            
        if draw:
            drawings.append(((ix,iy),size,colour))
        
    cv2.imshow("cam feed", frame)
cap.release()
cv2.destroyAllWindows()