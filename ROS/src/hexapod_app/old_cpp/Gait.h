#ifndef __GAIT_H__
#define __GAIT_H__

#include "Ogre.h"
#include "Robot.h"
#include <vector>

using namespace std;

#define PI 3.14159265

class Gait
{
public:
	typedef enum 
	{
		Idle,
		GoingUp,
		GoingForward,
		GoingDown,
		GoingBack,
		LiftingLegs
	} LegState;

	Gait();
	virtual ~Gait();

	virtual void destroy() = 0;
	static void destroyAll();

	virtual void handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt ) = 0;

protected:
	static LegState legState_;
	static Ogre::Radian legVelocity_;
	static Ogre::Radian vertAngle_;
	static Ogre::Radian horizAngle_;

	static std::vector<Gait*> gaitList_;
};

#endif // __GAIT_H__
