///////////////////////////////////////////////////////////
//  Robot.cpp
//  Implementation of the Class Robot
//  Created on:      17-Aug-2008 9:09:56 p.m.
//  Original author: jeremy
///////////////////////////////////////////////////////////

#include "Robot.h"

Robot::Robot(Ogre::SceneManager* sceneMgr)
{
	sceneMgr_ = sceneMgr;
	frontRightLeg_ = NULL;
	frontLeftLeg_ = NULL;
	middleRightLeg_ = NULL;
	middleLeftLeg_ = NULL;
	backRightLeg_ = NULL;
	backLeftLeg_ = NULL;
}

Robot::~Robot()
{
	if(frontRightLeg_)
	{
		delete frontRightLeg_;
		frontRightLeg_ = NULL;
	}

	if(frontLeftLeg_)
	{
		delete frontLeftLeg_;
		frontLeftLeg_ = NULL;
	}

	if(middleRightLeg_)
	{
		delete middleRightLeg_;
		middleRightLeg_ = NULL;
	}

	if(middleLeftLeg_)
	{
		delete middleLeftLeg_;
		middleLeftLeg_ = NULL;
	}

	if(backRightLeg_)
	{
		delete backRightLeg_;
		backRightLeg_ = NULL;
	}

	if(backLeftLeg_)
	{
		delete backLeftLeg_;
		backLeftLeg_ = NULL;
	}
}

void Robot::makeRobot()
{	
	Ogre::Entity *bodyEnt = sceneMgr_->createEntity("Body", "Body.mesh");
	bodyNode_ = sceneMgr_->getRootSceneNode()->createChildSceneNode("BodyNode");
	bodyNode_->attachObject(bodyEnt);

	frontRightLeg_ = new Leg(Right,75,bodyNode_,sceneMgr_);
	middleRightLeg_ = new Leg(Right,0,bodyNode_,sceneMgr_);
	backRightLeg_ = new Leg(Right,-75,bodyNode_,sceneMgr_);
	frontLeftLeg_ = new Leg(Left,75,bodyNode_,sceneMgr_);
	middleLeftLeg_ = new Leg(Left,0,bodyNode_,sceneMgr_);
	backLeftLeg_ = new Leg(Left,-75,bodyNode_,sceneMgr_);

}

