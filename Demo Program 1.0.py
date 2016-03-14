import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    cap.open()
    
def findBlobs(frame):
    # finds the blobs in the frame
    detector = cv2.SimpleBlobDetector_create()
    # sets up the detector with simple blob detection
    keypoints = detector.detect(frame)
    # finds the blobs
    blobsInFrame = cv2.drawKeypoints(frame, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #draws a blue circle around the detected blobs
    return blobsInFrame

while(True):
    ret, frame = cap.read()
    # Capture the video from the camera frame-by-frame

    # Stuff that we do to the frame goes here
    foundBlobs = findBlobs(frame)
    
    cv2.imshow('Keypoints', foundBlobs)
    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




#plan:
#    - get a feed of the camera thrown up where we can see the tracker working
#
#    - detect blobs of black and white
#    
#    - draw a circle around them and follow them with the circle
#        to draw a circle:
#            img = cv2.circle(img,(x coord, y coord), radius,
#               (colour as tuple in BGR (0,0,255)), thickness)
#            
#    - if there are more than one white blob or one black blobn throw an error
#        'Too many blobs!' - might be harder that I thought.....
