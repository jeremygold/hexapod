#include "CrabCrawlRight.h"

CrabCrawlRight* CrabCrawlRight::instance_ = NULL;

CrabCrawlRight::CrabCrawlRight()
{
	maxVertAngle_ = ( PI / 16 );
	minVertAngle_ = ( -PI / 16 );
	maxHorizAngle_ = ( PI / 8 );
	minHorizAngle_ = ( -PI / 8);
}

CrabCrawlRight::~CrabCrawlRight()
{
}

CrabCrawlRight* CrabCrawlRight::instance()
{
	if( instance_ == NULL )
	{
		instance_ = new CrabCrawlRight();
	}
	return instance_;
}

void CrabCrawlRight::destroy()
{
	if( instance_ != NULL )
	{
		delete instance_;
		instance_ = NULL;
	}
}

void CrabCrawlRight::handleFrameCallback( Robot* robot, const Ogre::FrameEvent &evt )
{
	Ogre::Radian vel = ( legVelocity_ * evt.timeSinceLastFrame / 2 );
	horizAngle_ = 0.0;

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
				legState_ = GoingForward;
			}
			break;

		case GoingForward:
			//printf( "GoingForward\n" );
			if( kneeAngle_ < maxHorizAngle_ )
			{
				// Keep going forward
				kneeAngle_ += vel;
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
				legState_ = GoingBack;
			}
			break;

		case GoingBack:
			//printf( "GoingBack\n" );
			if( kneeAngle_ > minHorizAngle_ )
			{
				// Keep going down
				kneeAngle_ -= vel;
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

	//printf( "Desired angles: %03.2f, %03.2f\n", vertAngle_.valueDegrees(), horizAngle_.valueDegrees());
	//printf( "LegState: %d\n", legState_ );

	robot->frontRightLeg_->setLegPos( horizAngle_, -vertAngle_, -kneeAngle_ );
	robot->middleRightLeg_->setLegPos( horizAngle_, vertAngle_, kneeAngle_ );
	robot->backRightLeg_->setLegPos( horizAngle_, -vertAngle_, -kneeAngle_ );
	robot->frontLeftLeg_->setLegPos( horizAngle_, vertAngle_, -kneeAngle_ );
	robot->middleLeftLeg_->setLegPos( horizAngle_, -vertAngle_, kneeAngle_ );
	robot->backLeftLeg_->setLegPos( horizAngle_, vertAngle_, -kneeAngle_ );
}

