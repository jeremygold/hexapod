#ifndef __SERVO_H__
#define __SERVO_H__

#include <Ogre.h>

class Servo 
{
public:
	Servo();
	void setDesiredAngle( Ogre::Radian angle );
	Ogre::Radian getDesiredAngle();

private:
	Ogre::Radian desiredAngle_;
};


#endif // __SERVO_H__
