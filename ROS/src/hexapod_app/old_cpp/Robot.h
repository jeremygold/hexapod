///////////////////////////////////////////////////////////
//  Robot.h
//  Implementation of the Class Robot
//  Created on:      17-Aug-2008 9:09:56 p.m.
//  Original author: jeremy
///////////////////////////////////////////////////////////

#pragma once

#include "Ogre.h"
#include "Leg.h"

class Robot
{
public:
	Robot(Ogre::SceneManager* sceneMgr);
	virtual ~Robot();

	void makeRobot();

	void handleFrameStarted(const Ogre::FrameEvent &evt);

	// TODO: Should these be private with accessors?
	Leg *frontRightLeg_;
	Leg *middleRightLeg_;
	Leg *backRightLeg_;
	Leg *frontLeftLeg_;
 	Leg	*middleLeftLeg_;
 	Leg	*backLeftLeg_;

private:
	Ogre::SceneNode* bodyNode_;
	Ogre::SceneManager* sceneMgr_;
};
