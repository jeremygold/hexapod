#ifndef __WALK_H__
#define __WALK_H__

#include "Gait.h"
#include "Ogre.h"
#include "Robot.h"

class Walk : public Gait
{
public:
	virtual ~Walk();

	static Walk* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );

protected:
	Walk();

private:
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;

	static Walk* instance_;
};

#endif // __WALK_H__
