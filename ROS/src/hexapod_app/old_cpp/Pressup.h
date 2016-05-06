#ifndef __PRESSUP_H__
#define __PRESSUP_H__

#include "Gait.h"

class Pressup: public Gait
{
public:
	virtual ~Pressup();
	static Pressup* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );
	
protected:
	Pressup();

private:
	static Pressup* instance_;
	
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
};

#endif // __PRESSUP_H__
