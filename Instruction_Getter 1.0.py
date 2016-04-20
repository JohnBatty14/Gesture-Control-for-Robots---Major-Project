import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    cap.open()  

def findWhiteBlobs(frame):
    params = cv2.SimpleBlobDetector_Params()
    params.filterByColor = 1
    params.blobColor = 255
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
    return keypoints

def findBlackBlobs(frame):
    params = cv2.SimpleBlobDetector_Params()
    params.filterByColor = 1
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
    return keypoints

def getTurnSignal(wKP, bKP):
    wX = wKP[0].pt[0] # x coord of white blob
    wY = wKP[0].pt[1] # y coord of white blob
    bX = bKP[0].pt[0] # x coord of black blob
    bY = bKP[0].pt[1] # y coord of black blob
    direction = "s" # value to be given to instruction

    if bX < wX: # through testing have found that the smaller value is towards the right on the screen.......
                #so if black is smaller then white is being held in the left hand..... because it's backwards remember dum dum
        print "LEFT YOU FOOLS!"
        direction = "l"
    elif bX > wX:
        print "RIGHT YOU FOOLS!"
        direction = "r"
    else:
        print "I dunno, maybe we should stop?"
        direction = "s"
    return direction

def instructions(wKP, bKP, n):
    wL = len(wKP)
    bL = len(bKP)
    length = wL + bL
    if n != length:
        print "The number of blobs is: %d" % (length)
        instruction = "s" # placeholder for the instruction to be given to the robot
        if bL == 2:
            print "STOP!"
            instruction = "s"
        elif bL == 1 and wL == 1:
            print "TURN!"
            instruction = getTurnSignal(wKP, bKP)
        elif wL == 2:
            print "FORWARD!"
            instruction = "f"
        else:
            print "No Recognised Intstruction Given. Therefore I shall STOP!"
            instruction = "s"
    n = length
    return n

n = 0
while(True):
    ret, frame = cap.read()
    
    # Stuff that we do to the frame goes here
    foundBKeypoints = findBlackBlobs(frame)
    foundWKeypoints = findWhiteBlobs(frame)

    #getKeypointObjectTag(foundBKeypoints)
    n = instructions(foundWKeypoints, foundBKeypoints, n)
    
    foundWBlobs = cv2.drawKeypoints(frame, foundWKeypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    foundBBlobs = cv2.drawKeypoints(frame, foundBKeypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    cv2.imshow('White keypoints', foundWBlobs)
    cv2.imshow('Black keypoints', foundBBlobs)
    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




#plan:
#    - get the keypoints from the blobs, they'll lead to the locations.
#
#    - once the keypoints have been translated into locations simple maths will reveal the relevency to each other blob1Y-blob2Y and so on and so forth
#    
#    - because black and white are detected seperately it'll be easy to tell which colour the presented blobs are
#            
#    - send the info to a function that'll calculate what the controller is telling the robot to do
#
#    - for now print the info out so we can see what the program thinks we are saying
