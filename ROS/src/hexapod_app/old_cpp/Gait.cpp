#include "Gait.h"

Gait::LegState Gait::legState_ = Idle;
Ogre::Radian Gait::legVelocity_ (PI);
Ogre::Radian Gait::vertAngle_ (0.0);
Ogre::Radian Gait::horizAngle_ (0.0);
vector<Gait*> Gait::gaitList_;

Gait::Gait()
{
	gaitList_.push_back( this );
}

Gait::~Gait()
{
}

void Gait::destroyAll()
{
	vector<Gait*>::iterator iterator = gaitList_.begin();

	while( iterator != gaitList_.end() )
	{
		Gait* nextGait = *iterator;
		//nextGait->destroy();
		iterator = gaitList_.erase( iterator );
		printf( "Deleted next Gait instance\n" );
	}
}
