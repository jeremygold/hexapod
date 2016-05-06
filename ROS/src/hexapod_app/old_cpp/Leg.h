#ifndef __LEG_H__
#define __LEG_H__

#include "Ogre.h"
#include "Servo.h"

extern const Ogre::Radian maxAngle;
extern const Ogre::Radian minAngle;
extern const Ogre::Radian maxHorizAngle;
extern const Ogre::Radian minHorizAngle;

typedef enum 
{
	Right,
	Left
} Side;

class Leg
{
public:
	Leg(Side side, Ogre::Real zpos, Ogre::SceneNode* bodyNode, Ogre::SceneManager *sceneMgr);
	~Leg();

	Servo* getHipVert();
	Servo* getHipHoriz();
	Servo* getKnee();

	void setHipVert( Servo* hipVert );
	void setHipHoriz( Servo* hipHoriz );
	void setKnee( Servo* knee );

	void setHipHorizAngle( Ogre::Radian angle );
	void setHipVertAngle( Ogre::Radian angle );
	void setKneeAngle( Ogre::Radian angle );
	double calcKneeAngle();

	void setLegPos( Ogre::Radian hipHorizAngle, Ogre::Radian hipVertAngle );
	void setLegPos( Ogre::Radian hipHorizAngle, Ogre::Radian hipVertAngle, Ogre::Radian kneeAngle );

private:
	Ogre::SceneNode* hipNode_;
	Ogre::SceneNode* thighNode_;
	Ogre::SceneNode* kneeNode_;
	Ogre::SceneNode* shinNode_;

	Servo* hipVert_;
	Servo* hipHoriz_;
	Servo* knee_;
	Side side_;
};

#endif // __LEG_H__

