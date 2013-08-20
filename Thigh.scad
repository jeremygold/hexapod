include <Shin.scad>

thighLength = 100.0;
thighWidth = servoWidth + 4 * wallThickness; // TODO - Build up from Shin dimensions + gap + wallThickness
thighDepth = axleShroudDiameter;

shinWidthClearance = 42.0; // Measured from top of axle shroud to outer surface of shin (with space for m3 washer on axle pin)

module thigh() {
// TODO - define all modules relative to center, and offset at the end
	difference() {
		thighMainBlock();
		thighMainCutout();
		thighTopCutouts();
		axleHole(0, -thighWidth / 2 + wallThickness / 2, m3Radius);
		axleHole(0, thighWidth / 2 - wallThickness / 2, m8Radius);
		# axleHole(-(thighLength - axleShroudDiameter), -thighWidth / 2 + wallThickness / 2, m3Radius);
		axleHole(-(thighLength - axleShroudDiameter), thighWidth / 2 - wallThickness / 2, m8Radius);
		// TODO - Cutout slot for servo bar - Does wall need to be a bith thicker on this side?
	}
}

module thighMainBlock() {
	hull() {
		for(x = [0, -thighLength+axleShroudDiameter]) {
			translate([x,0,0]) rotate([90,0,0])cylinder(h=(servoWidth + 4* wallThickness), r=(axleShroudDiameter / 2), center=true);
		}
	}
}

module axleHole(xOffset, yOffset, radius) {
	// TODO - Update to appropriate radii either side
	translate([xOffset, yOffset, 0])
		rotate([90,0,0])
			# cylinder(h=(wallThickness + differencePadding), r=radius, center=true);
}

module thighMainCutout() {
	translate([-thighLength / 2 + axleShroudDiameter / 2, 0, -wallThickness]) {
	  difference() {
		// Cutout most of the bottom, but leave a supporting strut
			cube([thighLength, thighWidth - wallThicknessEitherSide, thighDepth], center=true);
			cube([wallThickness, thighWidth, thighDepth], center=true);
		}
	}
}

module thighTopCutouts() {
	for(x=[-(thighLength / 3), (thighLength / 3)]) {
		translate([x - (thighLength / 2 - axleShroudDiameter /2), 0, thighDepth / 2 - wallThickness / 2])
			roundedCube((thighLength / 3 + axleShroudDiameter / 2), thighWidth - wallThicknessEitherSide, wallThickness + differencePadding, 5);
	}
}

thigh();

% rotate([0,0,0]) translate([axleXOffset,0,0]) shin();

