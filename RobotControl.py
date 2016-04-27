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
    if y == 0:
        x = 'STOP'
    else:
        x = 'FORWARD'
    return x

# STOP function
def stopFunc():
    #some code.....
    turnrate = 0.0
    speed = 0.000
    
# FORWARD function
def forwardFunc():
    #some code.....
    turnrate = 0.0
    speed = 0.500
    
# LEFT function
def leftFunc():
    #some code.....
    turnrate = -20.0
    speed = 0.100
    
# RIGHT function
def rightFunc():
    #some code.....
    turnrate = 20.0
    speed = 0.100
    
# choose instruction function
def setInstruction(n):
    instruction = getinstruction(n)
    if instruction == 'STOP':
        stopFunc()
    elif instruction == 'FORWARD':
        forwardFunc()
    elif instruction == 'LEFT':
        leftFunc()
    elif instruction == 'RIGHT':
        rightFunc()
    
# rest of code
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

while(True):
    n = 1
    setInstruction(n)
    p.set_smd_vel(speed, 0.0, turnrate * math.pi / 180.0, 1)

