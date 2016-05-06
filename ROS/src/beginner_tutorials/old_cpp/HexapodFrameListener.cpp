#include "HexapodFrameListener.h"

#include "CrabCrawlLeft.h"
#include "CrabCrawlRight.h"
#include "ForwardLeft.h"
#include "ForwardRight.h"
#include "Jump.h"
#include "Pressup.h"
#include "Rock.h"
#include "RotateLeft.h"
#include "RotateRight.h"
#include "WalkBackwards.h"
#include "Walk.h"

////////////////////////////////////////////////////////////////////////////////
bool HexapodFrameListener::frameStarted(const FrameEvent &evt)
{
	currentGait_->handleFrameCallback(robot_,evt);

	return ExampleFrameListener::frameStarted(evt);
}

////////////////////////////////////////////////////////////////////////////////
bool HexapodFrameListener::processUnbufferedKeyInput(const FrameEvent& evt)
{
	Real moveScale = mMoveScale;
	//Real bodyRotate = 60.0 * evt.timeSinceLastFrame;
	
	if(mKeyboard->isKeyDown(OIS::KC_LSHIFT))
		moveScale *= 10;

	if(mKeyboard->isKeyDown(OIS::KC_A))
		mTranslateVector.x = -moveScale;	// Move camera left

	if(mKeyboard->isKeyDown(OIS::KC_D))
		mTranslateVector.x = moveScale;	// Move camera RIGHT

	/*
	if(mKeyboard->isKeyDown(OIS::KC_UP) || mKeyboard->isKeyDown(OIS::KC_W) )
		bodyNode_->pitch(Degree(bodyRotate), Node::TS_LOCAL);

	if(mKeyboard->isKeyDown(OIS::KC_DOWN) || mKeyboard->isKeyDown(OIS::KC_S) )
		bodyNode_->pitch(-Degree(bodyRotate), Node::TS_LOCAL);
		*/

	if(mKeyboard->isKeyDown(OIS::KC_PGUP))
		mTranslateVector.y = moveScale;	// Move camera up

	if(mKeyboard->isKeyDown(OIS::KC_PGDOWN))
		mTranslateVector.y = -moveScale;	// Move camera down

	/*
	if(mKeyboard->isKeyDown(OIS::KC_RIGHT))
		bodyNode_->yaw(Degree(bodyRotate), Node::TS_LOCAL);

	if(mKeyboard->isKeyDown(OIS::KC_LEFT))
		bodyNode_->yaw(-Degree(bodyRotate), Node::TS_LOCAL);
		*/

/*

	if(mKeyboard->isKeyDown(OIS::KC_RIGHT))
		mCamera->yaw(-mRotScale);

	if(mKeyboard->isKeyDown(OIS::KC_LEFT))
		mCamera->yaw(mRotScale);
*/
	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD8))
	{
		currentGait_ = Walk::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD5))
	{
		currentGait_ = Pressup::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD0))
	{
		currentGait_ = Rock::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD9))
	{
		currentGait_ = ForwardRight::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD7))
	{
		currentGait_ = ForwardLeft::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD1))
	{
		currentGait_ = RotateLeft::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD3))
	{
		currentGait_ = RotateRight::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD2))
	{
		currentGait_ = WalkBackwards::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD6))
	{
		currentGait_ = CrabCrawlRight::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_NUMPAD4))
	{
		currentGait_ = CrabCrawlLeft::instance();
	}

	if( mKeyboard->isKeyDown(OIS::KC_ADD))
	{
		currentGait_ = Jump::instance();
	}


	if( mKeyboard->isKeyDown(OIS::KC_ESCAPE) || mKeyboard->isKeyDown(OIS::KC_Q) )
		return false;

	// Return true to continue rendering
	return true;

}

////////////////////////////////////////////////////////////////////////////////
bool HexapodFrameListener::processUnbufferedMouseInput(const FrameEvent& evt)
{
	// Rotation factors, may not be used if the second mouse button is pressed
	// 2nd mouse button - slide, otherwise rotate
	const OIS::MouseState &ms = mMouse->getMouseState();
	if( ms.buttonDown( OIS::MB_Right ) )
	{
		mTranslateVector.x += ms.X.rel * 0.13;
		mTranslateVector.y -= ms.Y.rel * 0.13;
	}
	else
	{
		mRotX = Degree(-ms.X.rel * 0.13);
		mRotY = Degree(-ms.Y.rel * 0.13);
#if OGRE_PLATFORM == OGRE_PLATFORM_IPHONE
		// Adjust the input depending upon viewport orientation
		Radian origRotY, origRotX;
		switch(mCamera->getViewport()->getOrientation())
		{
			case Viewport::OR_LANDSCAPELEFT:
				origRotY = mRotY;
				origRotX = mRotX;
				mRotX = origRotY;
				mRotY = -origRotX;
				break;
			case Viewport::OR_LANDSCAPERIGHT:
				origRotY = mRotY;
				origRotX = mRotX;
				mRotX = -origRotY;
				mRotY = origRotX;
				break;

				// Portrait doesn't need any change
			case Viewport::OR_PORTRAIT:
			default:
				break;
		}
#endif
	}

	return true;
}
////////////////////////////////////////////////////////////////////////////////
