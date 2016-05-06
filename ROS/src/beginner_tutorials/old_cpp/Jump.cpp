#include "Jump.h"

Jump* Jump::instance_ = NULL;

Jump::Jump()
{
	maxVertAngle_ = ( pi / 16 );
	minVertAngle_ = ( -pi / 16 );
	maxHorizAngle_ = ( pi / 8 );
	minHorizAngle_ = ( -pi / 8);
	timeToWait_ = 0.0;
}

Jump::~Jump()
{
}

Jump* Jump::instance()
{
	if( instance_ == NULL )
	{
		instance_ = new Jump();
	}
	return instance_;
}

void Jump::destroy()
{
	if( instance_ != NULL )
	{
		delete instance_;
		instance_ = NULL;
	}
}

void Jump::handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt )
{
	timeToWait_ -= evt.timeSinceLastFrame;

	Ogre::Radian vel = ( legVelocity_ * evt.timeSinceLastFrame / 2 );

	Ogre::Radian horizAngle = Ogre::Radian( 0.0 );

	Ogre::Radian minJumpAngle( -pi / 4 );
	Ogre::Radian maxJumpAngle( pi / 4 );
	Ogre::Radian middleJumpAngle( 0.0 );

	if( timeToWait_ < 0 )
	{
		switch( legState_ )
		{
			case GoingUp:
				//printf( "GoingUp\n" );
				if( vertAngle_ < maxJumpAngle )
				{
					// Keep going up
					vertAngle_ += vel;
				}
				else
				{
					legState_ = GoingDown;
					timeToWait_ = 1.0;
				}
				break;

			case GoingDown:
				//printf( "GoingDown\n" );
				if( vertAngle_ > minJumpAngle )
				{
					// Keep going down
					vertAngle_ -= vel * 7;
				}
				else
				{
					legState_ = LiftingLegs;
				}
				break;

			case LiftingLegs:
				if( vertAngle_ < middleJumpAngle )
				{
					vertAngle_ += vel * 7;
				}
				else
				{
					legState_ = GoingUp;
					//timeToWait_ = 2.0;
				}
				break;

			default:
				legState_ = GoingUp;
				// TODO: Do I need to reset angles to 0 as well?
				break;
		}
	}
	else
	{
		// No action - Just waiting...
	}

	robot->frontRightLeg->setLegPos( horizAngle, vertAngle_ );
	robot->middleRightLeg->setLegPos( horizAngle, vertAngle_ );
	robot->backRightLeg->setLegPos( horizAngle, vertAngle_ );
	robot->frontLeftLeg->setLegPos( horizAngle, vertAngle_ );
	robot->middleLeftLeg->setLegPos( horizAngle, vertAngle_ );
	robot->backLeftLeg->setLegPos( horizAngle, vertAngle_ );
}

