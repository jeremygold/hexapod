#ifndef __FORWARDRIGHT_H__
#define __FORWARDRIGHT_H__

#include "Gait.h"
#include "Ogre.h"
#include "Robot.h"

class ForwardRight : public Gait
{
public:
	virtual ~ForwardRight();

	static ForwardRight* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );

protected:
	ForwardRight();

private:
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;

	static ForwardRight* instance_;
};

#endif // __FORWARDRIGHT_H__
