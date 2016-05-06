#include "Ogre.h"
#include "OgreSceneNode.h"
#include "Leg.h"
#include "Robot.h"
#include <string>

const double PI = 3.1415926;

Leg::Leg(Side side, Ogre::Real zpos, Ogre::SceneNode *bodyNode, Ogre::SceneManager *sceneMgr)
{
	// TODO: Make unique entity names for each segment
	side_ = side;

	std::string legId = "";
	if(zpos == 0.0)
	{
		legId += "Middle";
	}
	else if(zpos > 0.0)
	{
		legId += "Front";
	}
	else if(zpos < 0.0)
	{
		legId += "Back";
	}

	if(side == Left)
	{
		legId += "Left";
	}
	else
	{
		legId += "Right";
	}

	printf("Creating leg '%s'\n", legId.c_str());
	
	std::string hipEntName = legId + "Hip";
	std::string hipNodeName = hipEntName + "Node";
	std::string thighEntName = legId + "Thigh";
	std::string thighNodeName = thighEntName + "Node";
	std::string kneeEntName = legId + "Knee";
	std::string kneeNodeName = kneeEntName + "Node";
	std::string shinEntName = legId + "Shin";
	std::string shinNodeName = shinEntName + "Node";

	Ogre::Vector3 hipOffset; 
	Ogre::Vector3 thighOffset;
	Ogre::Vector3 kneeOffset;
	Ogre::Vector3 shinOffset;
	Ogre::Entity *hipNode;

	Ogre::Degree thighYaw(0);
	
	if(side == Right)
	{
		hipOffset = Ogre::Vector3(25,0,0+zpos);
		thighOffset = Ogre::Vector3(12,8,8);
		kneeOffset = Ogre::Vector3(40,0,0);
		shinOffset = Ogre::Vector3(0,0,0);

		hipNode = sceneMgr->createEntity(hipEntName.c_str(),"RightHip.mesh");
	}
	else
	{
		hipOffset = Ogre::Vector3(-25,0,0+zpos);
		thighOffset = Ogre::Vector3(-12,8,8);
		kneeOffset = Ogre::Vector3(40,0,0);
		shinOffset = Ogre::Vector3(0,0,0);

		hipNode = sceneMgr->createEntity(hipEntName.c_str(),"LeftHip.mesh");

		thighYaw = Ogre::Degree(180);
	}

	hipNode_ = bodyNode->createChildSceneNode(hipNodeName.c_str(),hipOffset);
	hipNode_->attachObject(hipNode);

	Ogre::Entity *thighEnt = sceneMgr->createEntity(thighEntName.c_str(), "Thigh.mesh");
	thighNode_ = hipNode_->createChildSceneNode(thighNodeName.c_str(),thighOffset);
	thighNode_->attachObject(thighEnt);
	thighNode_->yaw(thighYaw);

	Ogre::Entity *kneeEnt = sceneMgr->createEntity(kneeEntName.c_str(), "Knee.mesh");
	kneeNode_ = thighNode_->createChildSceneNode(kneeNodeName.c_str(),kneeOffset);
	kneeNode_->attachObject(kneeEnt);

	Ogre::Entity *shinEnt = sceneMgr->createEntity(shinEntName.c_str(),"Shin.mesh");
	Ogre::SceneNode *shinNode = kneeNode_->createChildSceneNode(shinNodeName.c_str(),shinOffset);
	shinNode->attachObject(shinEnt);

	hipVert_ = new Servo();
	hipHoriz_ = new Servo();
	knee_ = new Servo();
}

Leg::~Leg()
{
	if( hipVert_ != NULL )
	{
		delete hipVert_;
		hipVert_ = NULL;
	}

	if( hipHoriz_ != NULL )
	{
		delete hipHoriz_;
		hipHoriz_ = NULL;
	}

	if( knee_ != NULL )
	{
		delete knee_;
		knee_ = NULL;
	}
}

Servo* Leg::getHipVert()
{
	return hipVert_;
}

Servo* Leg::getHipHoriz()
{
	return hipHoriz_;
}

Servo* Leg::getKnee()
{
	return knee_;
}

void Leg::setHipVert( Servo* hipVert )
{
	hipVert_ = hipVert;
}

void Leg::setHipHoriz( Servo* hipHoriz )
{
	hipHoriz_ = hipHoriz;
}

void Leg::setKnee( Servo* knee )
{
	knee_ = knee;
}


void Leg::setHipHorizAngle( Ogre::Radian angle )
{
	// TODO: Apply these angles to SceneNodes as well - Might need to keep track of current position using servo, and then work out how much to add (yaw() is relative to current pos)
	Ogre::Radian currentAngle = hipHoriz_->getDesiredAngle();

	if( hipHoriz_ != NULL )
	{
		if( side_ == Right )
		{
			hipHoriz_->setDesiredAngle( angle );
		}
		else
		{
			hipHoriz_->setDesiredAngle( -angle );
		}
	}

	Ogre::Degree deltaAngle = (currentAngle-hipHoriz_->getDesiredAngle());
	hipNode_->yaw(deltaAngle, Ogre::Node::TS_LOCAL);
}


void Leg::setHipVertAngle( Ogre::Radian angle )
{
	Ogre::Radian currentAngle = hipVert_->getDesiredAngle();

	if( hipVert_ != NULL )
	{
		hipVert_->setDesiredAngle( -angle );
	}

	Ogre::Degree deltaAngle = (currentAngle - hipVert_->getDesiredAngle());
	thighNode_->roll(deltaAngle, Ogre::Node::TS_LOCAL);
}


void Leg::setKneeAngle( Ogre::Radian angle )
{
	Ogre::Radian currentAngle = knee_->getDesiredAngle();

	if( knee_ != NULL )
	{
		knee_->setDesiredAngle( angle );
	}

	Ogre::Degree deltaAngle = (currentAngle - knee_->getDesiredAngle());
	kneeNode_->roll(deltaAngle, Ogre::Node::TS_LOCAL);
}

double Leg::calcKneeAngle()
{
	double result;

	// TODO: Work these out for blender model
	Ogre::Vector3 upperArmSize = Ogre::Vector3(40,0,0);
	Ogre::Vector3 lowerArmSize = Ogre::Vector3(0,40,0);
	
	Ogre::Radian maxAngle = Ogre::Radian( 0.0 );
	Ogre::Radian maxHorizAngle = Ogre::Radian( 0.0 );

	result =  -hipVert_->getDesiredAngle().valueRadians();
	double alpha = acos( ( upperArmSize.x * ( cos( fabs( hipVert_->getDesiredAngle().valueRadians() ) ) - cos( maxAngle.valueRadians() ) ) ) / lowerArmSize.y );
	double omega = acos( ( upperArmSize.x * ( cos( fabs( hipHoriz_->getDesiredAngle().valueRadians()  ) ) - cos( maxHorizAngle.valueRadians() ) ) ) / lowerArmSize.y );

	//if( side_ == Left )
	//{
		//result += alpha;
		//result += omega;
		//result -= PI;
	//}
	//else
	//{
		result -= alpha;
		result -= omega;
		result += PI;
	//}

	return result;
}

void Leg::setLegPos( Ogre::Radian hipHorizAngle, Ogre::Radian hipVertAngle )
{
	setHipHorizAngle( hipHorizAngle );
	setHipVertAngle( hipVertAngle );
	setKneeAngle(Ogre::Radian(calcKneeAngle()));
}

void Leg::setLegPos( Ogre::Radian hipHorizAngle, Ogre::Radian hipVertAngle, Ogre::Radian kneeAngle )
{
	setHipHorizAngle( hipHorizAngle );
	setHipVertAngle( hipVertAngle );
	setKneeAngle( kneeAngle );
}

