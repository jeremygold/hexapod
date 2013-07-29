$fn=40;

// All dimensions in mm
servoHeight = 32.0;
servoWidth = 35.0;
servoDepth = 16.9;
mountingTabWidth = 50.8;
mountingTabHeight = 3.5;
axleShroudHeight = 3.0;
axleShroudDiameter = servoDepth;
// Align outside of shroud with main body of servo
axleXOffset = servoWidth / 2 - axleShroudDiameter / 2;

gearShroudXOffset = axleXOffset - 10.0;
gearShroudDiameter = 4.6;
gearShroudHeight = axleShroudHeight;

module servoBody() {
  union() {
	  // The main body of the servo
		cube([servoWidth, servoHeight, servoDepth], center=true);
		
		// The mounting tabs either side
		translate([0, servoHeight / 2 - mountingTabHeight / 2, 0]) {
			cube([mountingTabWidth, mountingTabHeight, servoDepth], center=true);
		}
	}
}

module axleShroud() {
  translate([-axleXOffset, servoHeight / 2 + axleShroudHeight / 2, 0]){
		rotate([90,0,0]) {
			cylinder(axleShroudHeight, axleShroudDiameter/2, axleShroudDiameter/2,center=true);
		}
	}
}

module gearShroud() {
	translate([-gearShroudXOffset, servoHeight / 2 + gearShroudHeight / 2, 0]){
		rotate([90,0,0]) {
			cylinder(gearShroudHeight, gearShroudDiameter/2, gearShroudDiameter/2,center=true);
		}
	}
}

// Main routine
union() {
	servoBody();
	axleShroud();
	gearShroud();
}


