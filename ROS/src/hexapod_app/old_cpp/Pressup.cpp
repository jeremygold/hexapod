#include "Pressup.h"

Pressup* Pressup::instance_ = NULL;

Pressup::Pressup()
{
	maxVertAngle_ = ( pi / 4 );
	minVertAngle_ = ( -pi / 4 );
}

Pressup::~Pressup()
{
}

Pressup* Pressup::instance()
{
	if( instance_ == NULL )
	{
		instance_ = new Pressup();
	}
	return instance_;
}

void Pressup::destroy()
{
	if( instance != NULL )
	{
		delete instance_;
		instance_ = NULL;
	}
}

void Pressup::handleFrameCallback( Robot* robot, const Ogre::FrameEvent& evt )
{
	Ogre::Radian vel = ( legVelocity_ * evt.timeSinceLastFrame / 2 );

	Ogre::Radian horizAngle = Ogre::Radian( 0.0 );

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
				legState_ = GoingDown;
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
				legState_ = GoingUp;
			}
			break;

		default:
			legState_ = GoingUp;
			// TODO: Do I need to reset angles to 0 as well?
			break;
	}

	robot->frontRightLeg->setLegPos( horizAngle, vertAngle_ );
	robot->middleRightLeg->setLegPos( horizAngle, vertAngle_ );
	robot->backRightLeg->setLegPos( horizAngle, vertAngle_ );
	robot->frontLeftLeg->setLegPos( horizAngle, vertAngle_ );
	robot->middleLeftLeg->setLegPos( horizAngle, vertAngle_ );
	robot->backLeftLeg->setLegPos( horizAngle, vertAngle_ );
}

