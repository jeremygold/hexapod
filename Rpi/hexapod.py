#!/usr/bin/env python
 
import time
import os

STEP = 5
DELAY = 0.005
offset = 290
CENTER = 90
SWING = 45
MIN = CENTER - SWING
MAX = CENTER + SWING

LEFT = 1
RIGHT = 0

frontLeftShin = 3
frontLeftThigh = 4
frontLeftHip = 5

frontRightHip = 6
frontRightThigh = 7
frontRightShin = 8
 
def pwm(pin, angle):
  # Compensate for 1000 - 2000us representing +/- 90 degrees, and ServoBlaster is in units of 10us
  pwmDelay = 150 + ((angle - 90) * 50 / 90)
  print "servo[" + str(pin) + "][" + str(angle) + "=" + str(pwmDelay*10) + "us]"
  cmd = "echo " + str(pin) + "=" + str(pwmDelay) + " > /dev/servoblaster"
  os.system(cmd)

def moveCenter(motor):
  pwm(motor,CENTER)

def moveTest(motor, side):
  for j in range(MIN, MAX, STEP):
    if side == LEFT:
      pwm(motor,j)
    else:
      pwm(motor,180-j)
    time.sleep(DELAY)

  for j in range(MAX, MIN, (STEP*-1)):
    if side == LEFT:
      pwm(motor,j)
    else:
      pwm(motor,180-j)
    time.sleep(DELAY)

  time.sleep(1)

def legUp():
  for j in range(MIN, MAX, STEP):
    pwm(frontLeftShin,j)
    pwm(frontLeftThigh,j)

    pwm(frontRightShin,(MAX - j) + MIN)
    pwm(frontRightThigh,(MAX - -j) + MIN)
    time.sleep(DELAY)

def legDown():
  for j in range(MAX, MIN, (STEP*-1)):
    pwm(frontLeftShin,j)
    pwm(frontLeftThigh,j)

    pwm(frontRightShin,(MAX - j) + MIN)
    pwm(frontRightThigh,(MAX - j) + MIN)
    time.sleep(DELAY)

def legForward():
  for j in range(MIN, MAX, STEP):
    pwm(frontLeftHip,j)
    pwm(frontRightHip,(MAX - j) + MIN)
    time.sleep(DELAY)

def legBack():
  for j in range(MAX, MIN, (STEP*-1)):
    pwm(frontLeftHip,j)
    pwm(frontRightHip,(MAX - j) + MIN)
    time.sleep(DELAY)

while True:
  # legUp()
  # legForward()
  # legDown()
  # legBack()
  moveCenter(frontLeftShin)
  moveCenter(frontLeftThigh)
  moveCenter(frontLeftHip)

  moveCenter(frontRightShin)
  moveCenter(frontRightThigh)
  moveCenter(frontRightHip)
  time.sleep(1)

  moveTest(frontLeftShin, LEFT)
  moveTest(frontLeftThigh, LEFT)
  moveTest(frontLeftHip, LEFT)

  moveTest(frontRightShin, RIGHT)
  moveTest(frontRightThigh, RIGHT)
  moveTest(frontRightHip, RIGHT)
  time.sleep(1)

