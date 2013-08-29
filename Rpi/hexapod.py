#!/usr/bin/env python
 
import time
import os

STEP = 1
DELAY = 0.001
 
def pwm(pin, angle):
  print "servo[" + str(pin) + "][" + str(angle) + "]"
  cmd = "echo " + str(pin) + "=" + str(angle) + " > /dev/servoblaster"
  os.system(cmd)

def legUpDown():
  for j in range(90, 170, STEP):
    pwm(1,j)
    pwm(2,j)
    # time.sleep(DELAY)
  for j in range(170, 90, (STEP*-1)):
    pwm(1,j)
    pwm(2,j)
    # time.sleep(DELAY)

def legForwardBack():
  for j in range(90, 170, STEP):
    pwm(3,j)
    # time.sleep(DELAY)
  for j in range(170, 90, (STEP*-1)):
    pwm(3,j)
    # time.sleep(DELAY)

while True:
  legUpDown()
  legForwardBack()

