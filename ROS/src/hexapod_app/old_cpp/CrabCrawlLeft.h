#ifndef __CRABCRAWLLEFT_H__
#define __CRABCRAWLLEFT_H__

#include "Gait.h"
#include "Ogre.h"
#include "Robot.h"

class CrabCrawlLeft : public Gait
{
public:
	virtual ~CrabCrawlLeft();

	static CrabCrawlLeft* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );

protected:
	CrabCrawlLeft();

private:
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;
	Ogre::Radian kneeAngle_;

	static CrabCrawlLeft* instance_;
};

#endif // __CRABCRAWLLEFT_H__
