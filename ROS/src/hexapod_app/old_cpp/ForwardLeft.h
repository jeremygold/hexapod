#ifndef __FORWARDLEFT_H__
#define __FORWARDLEFT_H__

#include "Gait.h"
#include "Ogre.h"
#include "Robot.h"

class ForwardLeft : public Gait
{
public:
	virtual ~ForwardLeft();

	static ForwardLeft* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );

protected:
	ForwardLeft();

private:
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;

	static ForwardLeft* instance_;
};

#endif // __FORWARDLEFT_H__
