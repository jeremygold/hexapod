#ifndef __ROTATERIGHT_H__
#define __ROTATERIGHT_H__

#include "Gait.h"
#include "Ogre.h"
#include "Robot.h"

class RotateRight : public Gait
{
public:
	virtual ~RotateRight();

	static RotateRight* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );

protected:
	RotateRight();

private:
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;

	static RotateRight* instance_;
};

#endif // __ROTATERIGHT_H__
