#ifndef __ROCK_H__
#define __ROCK_H__

#include "Gait.h"

class Rock: public Gait
{
public:
	virtual ~Rock();
	static Rock* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );
	
protected:
	Rock();

private:
	static Rock* instance_;

	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;
};

#endif // __ROCK_H__
