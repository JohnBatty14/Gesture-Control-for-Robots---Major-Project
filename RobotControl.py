import math
from playerc import *

#I need this code to take in 4 commands:
#    FORWARD
#    STOP
#    LEFT
#    RIGHT
#and implement them as instructions to the robot.

# get instruction function
def getInstruction(y):
    y = y + 1
    return y

# STOP function
def stopFunc():
    print 'STOP'
    #The below code would set the desired speed and turnrate for the robot
    turnrate = 0.0
    speed = 0.000
    
# FORWARD function
def forwardFunc():
    print 'FORWARD'
    #The below code would set the desired speed and turnrate for the robot
    turnrate = 0.0
    speed = 0.500
    
# LEFT function
def leftFunc():
    print 'LEFT'
    #The below code would set the desired speed and turnrate for the robot
    turnrate = -20.0
    speed = 0.100
    
# RIGHT function
def rightFunc():
    print 'RIGHT'
    #The below code would set the desired speed and turnrate for the robot
    turnrate = 20.0
    speed = 0.100
    
# choose instruction function
def setInstruction(n):
    if n == 0:
        stopFunc()
    elif n == 1:
        forwardFunc()
    elif n == 2:
        leftFunc()
    elif n == 3:
        rightFunc()
    
# Create a client object
c = playerc_client(None, 'localhost', 6665)
# Connect it
if c.connect() != 0:
  raise playerc_error_str()

# Create a proxy for position2d:0
p = playerc_position2d(c,0)
if p.subscribe(PLAYERC_OPEN_MODE) != 0:
  raise playerc_error_str()

#rate at which robot turns and speed at which it moves
turnrate = 0
speed = 0
n = -1

while(n != 4):
    n = getInstruction(n)
    setInstruction(n)
    # This line would set the robot instruction which it would then implement.
    p.set_smd_vel(speed, 0.0, turnrate * math.pi / 180.0, 1)
