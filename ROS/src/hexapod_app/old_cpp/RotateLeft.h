#ifndef __ROTATELEFT_H__
#define __ROTATELEFT_H__

#include "Gait.h"
#include "Ogre.h"
#include "Robot.h"

class RotateLeft : public Gait
{
public:
	virtual ~RotateLeft();

	static RotateLeft* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );

protected:
	RotateLeft();

private:
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;

	static RotateLeft* instance_;
};

#endif // __ROTATELEFT_H__
