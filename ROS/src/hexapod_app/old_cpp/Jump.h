#ifndef __JUMP_H__
#define __JUMP_H__

#include "Gait.h"
#include "Ogre.h"
#include "Robot.h"

class Jump : public Gait
{
public:
	virtual ~Jump();

	static Jump* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );

protected:
	Jump();

private:
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;
	Ogre::Real timeToWait_;

	static Jump* instance_;
};

#endif // __JUMP_H__
