#ifndef __CRABCRAWLRIGHT_H__
#define __CRABCRAWLRIGHT_H__

#include "Gait.h"
#include "Ogre.h"
#include "Robot.h"

class CrabCrawlRight : public Gait
{
public:
	virtual ~CrabCrawlRight();

	static CrabCrawlRight* instance();
	void destroy();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt );

protected:
	CrabCrawlRight();

private:
	Ogre::Radian maxVertAngle_;
	Ogre::Radian minVertAngle_;
	Ogre::Radian maxHorizAngle_;
	Ogre::Radian minHorizAngle_;
	Ogre::Radian kneeAngle_;

	static CrabCrawlRight* instance_;
};

#endif // __CRABCRAWLRIGHT_H__
