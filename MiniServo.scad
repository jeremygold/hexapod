$fn=40;

// All dimensions in mm

// Overall dimensions of servo (excluding mounting tabs and axle shroud
servoHeight = 32.0;
servoWidth = 35.0;
servoDepth = 16.9;

// Additional dimensions for mounting tabs
mountingTabWidth = 50.8;
mountingTabHeight = 3.5;

// Axle shroud dimensions
axleShroudHeight = 3.0;
axleShroudDiameter = servoDepth;
// Align outside of shroud with main body of servo
axleXOffset = servoWidth / 2 - axleShroudDiameter / 2;

// Axle dimensions
axleDiameter = 6.0;
axleHeight = 4.0;  // Above Shroud

gearShroudXOffset = axleXOffset - 10.0;
gearShroudDiameter = 4.6;

// Rectangular pockets for mounting holes
mountingHolePocketWidth = 7.7;
mountingHolePocketDepth = 6.6;
mountingHolePocketHeight = 1.0;

// Gap between outer edge and pockets
mountingHolePocketInset = 1.3;

mhX = mountingTabWidth / 2 - mountingHolePocketWidth / 2;
mhY = servoDepth / 2 - mountingHolePocketDepth / 2 - mountingHolePocketInset;

mountingHoleDiameter = 4.0;
mountingHoleCutoutWidth = 2.0;

function signum(x) = (x < 0)?-1:(x > 0)?1:0;

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

module axleAndGearShroud(height, yOffset) {
	union() {
		translate([-axleXOffset, yOffset + height / 2, 0]){
			rotate([90,0,0]) {
				cylinder(height, axleShroudDiameter/2, axleShroudDiameter/2,center=true);
			}
		}
		translate([-gearShroudXOffset, yOffset+ height / 2, 0]){
			union() {
				rotate([90,0,0]) {
					cylinder(height, gearShroudDiameter/2, gearShroudDiameter/2,center=true);
				}
				translate([-gearShroudDiameter/2,0,0]) cube([gearShroudDiameter, height, gearShroudDiameter], center=true);
			}
		}
	}
}

module axle() {
  translate([-axleXOffset, servoHeight / 2 + axleShroudHeight + axleHeight / 2, 0]){
		rotate([90,0,0]) {
			cylinder(axleHeight, axleDiameter/2, axleDiameter/2,center=true);
		}
	}
}

module mountingDetail() {
	for(x = [-mhX, mhX]) {
		for(z = [-mhY, mhY]) {
			translate([x, servoHeight / 2 - mountingHolePocketHeight / 2, z]) {
				union() {
					// Rectangular pocket
					cube([mountingHolePocketWidth, mountingHolePocketHeight, mountingHolePocketDepth], center=true);

					// Actual mounting hole
					rotate([90,0,0]) cylinder(mountingTabHeight * 2, mountingHoleDiameter / 2, mountingHoleDiameter / 2, center=true);

					// Cutout to edge
					translate([signum(x) * mountingHolePocketWidth / 2, 0, 0]) cube([mountingHolePocketWidth, mountingTabHeight * 2,mountingHoleCutoutWidth], center=true);
				}
			}
		}
	}
}

module mountingBoltHoles(height, yOffset) {
	for(x = [-mhX, mhX]) {
		for(z = [-mhY, mhY]) {
			translate([x, yOffset, z]) {
					// Actual mounting hole
					rotate([90,0,0]) cylinder(height, mountingHoleDiameter / 2, mountingHoleDiameter / 2, center=true);
			}
		}
	}
}

// Main routine
module MiniServo() {
	difference() {
		union() {
			servoBody();
			axleAndGearShroud(axleShroudHeight, servoHeight / 2);
			axle();
		}

		union() {
			mountingDetail();
			mountingBoltHoles(mountingTabHeight * 2, servoHeight / 2 - mountingHolePocketHeight / 2);
		}
	}
}

//MiniServo();
