#include "Servo.h"

Servo::Servo() 
{
}

void Servo::setDesiredAngle( Ogre::Radian angle )
{
	desiredAngle_ = angle;
}

Ogre::Radian Servo::getDesiredAngle()
{
	return desiredAngle_;
}

