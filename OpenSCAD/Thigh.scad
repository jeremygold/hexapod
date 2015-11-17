include <HexapodDimensions.scad>
include <Shin.scad>

shinWidthClearance = 42.0; // Measured from top of axle shroud to outer surface of shin (with space for m3 washer on axle pin)

thighLength = 85.0;
// TODO - Build up from Shin dimensions + gap + wallThickness
thighWidth = shinWidthClearance + 3 * wallThickness; 
thighDepth = axleShroudDiameter;

servoBarSpacing = 0.2;

module thigh() {
// TODO - define all modules relative to center, and offset at the end
	difference() {
		thighMainBlock();
		thighMainCutout();
		thighTopCutouts();

// TODO - Refactor out cutoutAxleHoles()
		axleHole(0, -thighWidth / 2 + wallThickness, m3Radius);
		axleHole(0, thighWidth / 2 - wallThickness, m8Radius);
		axleHole(-(thighLength - axleShroudDiameter), -thighWidth / 2 + wallThickness , m3Radius);
		axleHole(-(thighLength - axleShroudDiameter), thighWidth / 2 - wallThickness, m8Radius);

		cutoutServoSlot(0);
		cutoutServoSlot(-thighLength + axleShroudDiameter);
	}
}

module thighMainBlock() {
// Construct main block as hull around two cylinders either end of the part
	hull() {
		for(x = [0, -thighLength+axleShroudDiameter]) {
			translate([x, wallThickness / 2,0]) 
			  rotate([90,0,0]) 
				  cylinder(h=(shinWidthClearance + 3 * wallThickness), r=(axleShroudDiameter / 2), center=true);
		}
	}
}

module thighMainCutout() {
	translate([-thighLength / 2 + axleShroudDiameter / 2, 0, -wallThickness]) {
		// Cutout most of the bottom, but leave a supporting strut
		union() {
			for(x = [-1,1]) {
				translate([x*(thighLength / 2 + wallThickness / 2), 0, 0]) {
					roundedCube(thighLength, shinWidthClearance, thighDepth + differencePadding, 5);
				}
			}
		}
	}
}

module cutoutServoSlot(xOffset) {
	translate([xOffset, thighWidth / 2, 0])
		rotate([90,0,0]) {
			hull() {
				cylinder(h=wallThickness + differencePadding, r=4.0 + servoBarSpacing, center=true);
				translate([-15,0,0]) cylinder(h=wallThickness + differencePadding, r=2.5 + servoBarSpacing, center=true);
				translate([15,0,0]) cylinder(h=wallThickness + differencePadding, r=2.5 + servoBarSpacing, center=true);
			}
		}
}

module axleHole(xOffset, yOffset, radius) {
	// TODO - Update to appropriate radii either side
	translate([xOffset, yOffset, 0])
		rotate([90,0,0])
			cylinder(h=(wallThickness + differencePadding), r=radius, center=true);
}

module thighTopCutouts() {
	for(x=[-(thighLength / 3), (thighLength / 3)]) {
		translate([x - (thighLength / 2 - axleShroudDiameter /2), 0, thighDepth / 2 - wallThickness / 2])
			roundedCube((thighLength / 3 + axleShroudDiameter / 2), thighWidth - 3 * wallThickness, wallThickness + differencePadding, 5);
	}
}

