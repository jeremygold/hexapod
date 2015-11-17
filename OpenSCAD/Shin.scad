include <MiniServo.scad>
include <utils.scad>

$fn=40;

// All dimensions in mm
wallThickness = 3;
wallThicknessEitherSide = 2 * wallThickness;

innerSizeTolerance = 0.4;
differencePadding = 0.1;

shinTopLength = mountingTabWidth + wallThicknessEitherSide;
shinBottomLength = 65;

footRadius = 5;
footCutoutOffset = 20;
footCutoutTopOffset = 5;
footCutoutBottomRadius = 3;

filletRadius = 2;

cutoutHeight = servoDepth + wallThicknessEitherSide + differencePadding;

module axleGearShroud() {
	union() {
		axleShroud();
		gearShroud();
	}
}

// Hole opposite axle that will be used for a pin that the thigh will rotate on

module cutoutAxleExtensionHole() {
	translate([-axleXOffset, -(servoHeight / 2), 0]){
		rotate([90,0,0]) {
			m3CskBolt(8);
		}
	}
}

module cutoutCableExtensionHole() {
	translate([-(shinTopLength / 2 - wallThickness / 2), 0, 0]) 
		rotate([0,90,0])
			roundedCube(12, 3, (wallThickness + differencePadding), 1);
}

// Main Shin Top section
module shinTopSection() {
	union() {
		difference(){
			// Main cube to carve from
			cube([shinTopLength,
					servoHeight + wallThicknessEitherSide, 
					servoDepth + wallThicknessEitherSide], center=true);

			// Cut out inner material to leave space for servo
			translate([0, 0, wallThickness / 2]) roundedCube(shinTopLength + innerSizeTolerance - wallThicknessEitherSide, servoHeight + innerSizeTolerance, servoDepth + innerSizeTolerance + wallThickness, 2);

			// Cutouts in base to minimise material required
			for(xPos = [-shinTopLength / 4, shinTopLength / 4]) {
				translate([xPos, 0, -(servoDepth + wallThickness) / 2]) 
					roundedCube(shinTopLength / 3, servoHeight - wallThickness, wallThickness + differencePadding, filletRadius);
			}

			// Cutout slot for Axle and Gear Shroud 
			hull() {
				translate([0,0,(servoDepth + wallThicknessEitherSide) / 2]) axleAndGearShroud(wallThickness + differencePadding * 2, servoHeight / 2 - differencePadding);
				axleAndGearShroud(wallThickness + differencePadding * 2, servoHeight / 2 - differencePadding);
			}

			// Cutout bolt holes
			mountingBoltHoles(wallThickness + differencePadding, servoHeight / 2 + wallThickness / 2, m3Radius);

			// Cutout bolt hole for pin opposite axle
			cutoutAxleExtensionHole();

			// Hole on top face for servo cable
			cutoutCableExtensionHole();
		}
	}
}

// Shin bottom section down to foot
module shinBottomSection() {
	difference() {

	  // Shin Tapered section down to foot.
		hull() {
			translate([shinTopLength / 2, 0, 0]) {
				cube([wallThickness, servoHeight + wallThicknessEitherSide, servoDepth + wallThicknessEitherSide], center=true);
			}
			translate([shinTopLength / 2 + shinBottomLength, 0, -(servoDepth + wallThicknessEitherSide) / 2 + footRadius]) {
				rotate([0,90,0]) cylinder(h=wallThickness, r=footRadius, center=true);
			}
		}

		// Hollow out the inside
		hull() {
			translate([shinTopLength / 2, 0, 0]) {
				cube([wallThickness + differencePadding, servoHeight, servoDepth], center=true);
			}

			// TODO - Cutout should be inside foot, so foot base is wallThickness.
			// TODO - Should include a hole for mounting a rubber foot
			translate([shinTopLength / 2 + shinBottomLength, 0, -(servoDepth + wallThicknessEitherSide) / 2 + footRadius]) {
				rotate([0,90,0]) cylinder(h=wallThickness + differencePadding, r=(footRadius - wallThickness), center=true);
			}
		}

		// Shin cutout created from hull of 3 cylinders
		hull() {
			translate([shinTopLength / 2 + shinBottomLength - footCutoutOffset, 0, 0])
				cylinder(h=cutoutHeight, r=footCutoutBottomRadius, center=true);

			for(ySide = [-1,1]) {
				translate([shinTopLength / 2 + footCutoutTopOffset, ySide * (servoHeight / 2 - 2 * wallThickness), 0]) 
				cylinder(h=cutoutHeight, r=filletRadius, center=true);
			}
		}
	}
}

module shin() {
	union() {
		shinTopSection();
		shinBottomSection();
	}
}

//% MiniServo();

mirror([0,1,0]) shin();


