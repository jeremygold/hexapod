#pragma once

#include "ExampleApplication.h"
#include "HexapodFrameListener.h"
#include "Robot.h"

class HexapodApplication: public ExampleApplication
{
	public:
		HexapodApplication(); 
		~HexapodApplication();

	protected:
		void createScene(void);
		void createFrameListener(void);

		SceneNode *hipNode_;
		SceneNode *thighNode_;
		SceneNode *kneeNode_;
		SceneNode *bodyNode_;
		Robot* robot_;
};


