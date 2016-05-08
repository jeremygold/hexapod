#include "Rock.h"

Rock* Rock::instance_ = NULL;

Rock::Rock()
{
	legVelocity_ = pi / 2;
	legState_ = GoingForward;
	horizAngle_ = 0;
	
	maxHorizAngle_ = ( pi / 3 );
	minHorizAngle_ = ( -pi / 3 );
}

Rock::~Rock()
{
}

Rock* Rock::instance()
{
	if( instance_ == NULL )
	{
		instance_ = new Rock();
	}
	return instance_;
}

void Rock::destroy()
{
	if( instance != NULL )
	{
		delete instance_;
		instance_ = NULL;
	}
}

void Rock::handleFrameCallback( Robot* robot, const Ogre::FrameEvent& evt )
{
	Ogre::Radian vel = ( legVelocity_ * evt.timeSinceLastFrame / 2 );

	Ogre::Radian vertAngle = Ogre::Radian( 0.0 );

	switch( legState_ )
	{
		case GoingForward:
			if( horizAngle_ < maxHorizAngle_ )
			{
				// Keep going forward
				horizAngle_ += vel;
			}
			else
			{
				legState_ = GoingBack;
			}
			break;

		case GoingBack:
			//printf( "GoingBack\n" );
			if( horizAngle_ > minHorizAngle_ )
			{
				// Keep going back
				horizAngle_ -= vel;
			}
			else
			{
				legState_ = GoingForward;
			}
			break;

		default:
			legState_ = GoingForward;
			// TODO: Do I need to reset angles to 0 as well?
			break;
	}

	robot->frontRightLeg->setLegPos( horizAngle_, vertAngle );
	robot->middleRightLeg->setLegPos( horizAngle_, vertAngle );
	robot->backRightLeg->setLegPos( horizAngle_, vertAngle );
	robot->frontLeftLeg->setLegPos( horizAngle_, vertAngle );
	robot->middleLeftLeg->setLegPos( horizAngle_, vertAngle );
	robot->backLeftLeg->setLegPos( horizAngle_, vertAngle );
}

