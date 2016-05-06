#ifndef __WALKBACKWARDS_H__
#define __WALKBACKWARDS_H__

#include "Gait.h"
#include "Ogre.h"
#include "Robot.h"

class WalkBackwards : public Gait
{
public:
	virtual ~WalkBackwards();

	static WalkBackwards* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );

protected:
	WalkBackwards();

private:
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;

	static WalkBackwards* instance_;
};

#endif // __WALKBACKWARDS_H__
