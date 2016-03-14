import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    cap.open()

def printBlobLoc(keypoints):
    for n in range(0, keypoints.size()):
        print "X Coord: %d" % (keypoints[n].pt.x)
        print "Y Coord: %d" % (keypoints[n].pt.y)


def findBlobs(frame):
    params = cv2.SimpleBlobDetector_Params()
    params.filterByColor = True
    params.blobColor = 0
    params.filterByInertia = True
    params.minInertiaRatio = 0.7
    params.filterByConvexity = True
    params.minConvexity = 0.8
    params.filterByCircularity = True
    params.minCircularity = 0.8
    params.filterByArea = True
    params.minArea = 900
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(frame)
    #printBlobLoc(keypoints)
    return keypoints

while(True):
    ret, frame = cap.read()

    # Stuff that we do to the frame goes here
    foundKeypoints = findBlobs(frame)   
    foundBlobs = cv2.drawKeypoints(frame, foundKeypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
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
