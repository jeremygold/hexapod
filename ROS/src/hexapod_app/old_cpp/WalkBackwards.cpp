#include "WalkBackwards.h"

WalkBackwards* WalkBackwards::instance_ = NULL;

WalkBackwards::WalkBackwards()
{
	maxVertAngle_ = ( pi / 16 );
	minVertAngle_ = ( -pi / 16 );
	maxHorizAngle_ = ( pi / 8 );
	minHorizAngle_ = ( -pi / 8);
}

WalkBackwards::~WalkBackwards()
{
}

WalkBackwards* WalkBackwards::instance()
{
	if( instance_ == NULL )
	{
		instance_ = new WalkBackwards();
	}
	return instance_;
}

void WalkBackwards::destroy()
{
	if( instance_ != NULL )
	{
		delete instance_;
		instance_ = NULL;
	}
}

void WalkBackwards::handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt )
{
	Ogre::Radian vel = ( legVelocity_ * evt.timeSinceLastFrame / 2 );
	switch( legState_ )
	{
		case GoingUp:
			//printf( "GoingUp\n" );
			if( vertAngle_ < maxVertAngle_ )
			{
				// Keep going up
				vertAngle_ += vel;
			}
			else
			{
				legState_ = GoingBack;
			}
			break;

		case GoingForward:
			//printf( "GoingForward\n" );
			if( horizAngle_ < maxHorizAngle_ )
			{
				// Keep going forward
				horizAngle_ += vel;
			}
			else
			{
				legState_ = GoingUp;
			}
			break;

		case GoingDown:
			//printf( "GoingDown\n" );
			if( vertAngle_ > minVertAngle_ )
			{
				// Keep going down
				vertAngle_ -= vel;
			}
			else
			{
				legState_ = GoingForward;
			}
			break;

		case GoingBack:
			//printf( "GoingBack\n" );
			if( horizAngle_ > minHorizAngle_ )
			{
				// Keep going down
				horizAngle_ -= vel;
			}
			else
			{
				legState_ = GoingDown;
			}
			break;

		default:
			legState_ = GoingUp;
			// TODO: Do I need to reset angles to 0 as well?
			break;
	}

	//printf( "Desired angles: %03.2f, %03.2f\n", vertAngle_.valueDegrees(), horizAngle_.valueDegrees());
	//printf( "LegState: %d\n", legState_ );

	robot->frontRightLeg->setLegPos( -horizAngle_, -vertAngle_ );
	robot->middleRightLeg->setLegPos( horizAngle_, vertAngle_ );
	robot->backRightLeg->setLegPos( -horizAngle_, -vertAngle_ );
	robot->frontLeftLeg->setLegPos( horizAngle_, vertAngle_ );
	robot->middleLeftLeg->setLegPos( -horizAngle_, -vertAngle_ );
	robot->backLeftLeg->setLegPos( horizAngle_, vertAngle_ );
}

