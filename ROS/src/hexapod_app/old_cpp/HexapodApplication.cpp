#include "HexapodApplication.h"
#include "HexapodFrameListener.h"
#include "Walk.h"

HexapodApplication::HexapodApplication()
{
}

HexapodApplication::~HexapodApplication()
{
	Gait::destroyAll();
}

void HexapodApplication::createFrameListener(void)
{
	printf("****** Creating frame listener ****** \n");

	// Create the FrameListener
	mFrameListener = new HexapodFrameListener(mWindow, mCamera, mSceneMgr);
	((HexapodFrameListener*)mFrameListener)->robot_ = robot_;
	((HexapodFrameListener*)mFrameListener)->currentGait_ = Walk::instance();
	mRoot->addFrameListener(mFrameListener);

	// Show the frame stats overlay
	mFrameListener->showDebugOverlay(true);
}

void HexapodApplication::createScene(void)
{
	printf("****** Creating scene ******\n");
	mSceneMgr->setAmbientLight( ColourValue( 1, 1, 1 ) );

	robot_ = new Robot(mSceneMgr);
	robot_->makeRobot();

	Light *light;
	light = mSceneMgr->createLight("Light1");
	light->setType(Light::LT_POINT);
	light->setPosition(Vector3(0, 250, 350));
	light->setDiffuseColour(1.0, 1.0, 1.0);
	light->setSpecularColour(1.0, 1.0, 1.0);
}


