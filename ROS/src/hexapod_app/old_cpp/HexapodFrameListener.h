#pragma once

#include "ExampleApplication.h"
#include "Robot.h"
#include "Gait.h"

class HexapodFrameListener : public ExampleFrameListener
{
	public:
		HexapodFrameListener(RenderWindow* win, Camera* cam, SceneManager *sceneMgr)
			: ExampleFrameListener(win, cam, false, false)
		{
		}

		// Overriding the default processUnbufferedKeyInput so the key updates we define
		// later on work as intended.
		bool processUnbufferedKeyInput(const FrameEvent& evt);

		// Overriding the default processUnbufferedMouseInput so the Mouse updates we define
		// later on work as intended. 
		bool processUnbufferedMouseInput(const FrameEvent& evt);

		bool frameStarted(const FrameEvent &evt);

		// TODO: Should frame listener have ref to application so it doesn't need it's own copy?
		Robot * robot_;
		Gait* currentGait_;

	protected:
		bool mMouseDown;       // Whether or not the left mouse button was down last frame
		Real mToggle;          // The time left until next toggle
		Real mRotate;          // The rotate constant
		Real mMove;            // The movement constant
		// TODO: rename mSceneMgr sceneMgr_
		SceneManager *mSceneMgr;   // The current SceneManager
		SceneNode *mCamNode;   // The SceneNode the camera is currently attached to

};

