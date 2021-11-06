import cv2 

cap = cv2.VideoCapture(0)
tracker_types = {
    'BOOSTING':cv2.TrackerBoosting_create,
    'MIL':cv2.TrackerMIL_create,
    'TLD':cv2.TrackerTLD_create,
    'MEDIANFLOW':cv2.TrackerMedianFlow_create,
    'CSRT':cv2.TrackerCSRT_create,      #* Slower but more accurate
    'MOSSE':cv2.TrackerMOSSE_create
}
#*To run below code please install:- pip install opencv-contrib-python==4.2.0.34
tracker = tracker_types['MOSSE']()

#* This frame is used to select an object which is going to be tracked.
success,img = cap.read()
bbox = cv2.selectROI('Tracking',img,False)
tracker.init(img,bbox)

while True:
    timer = cv2.getTickCount()
    success,img = cap.read()

    success,bbox = tracker.update(img)
    if success:
        x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
    else:
        cv2.putText(img,'Object Lost',(75,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),2)    
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)

    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),2)
    cv2.imshow('Tracking',img)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break
