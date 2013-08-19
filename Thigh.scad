include <Shin.scad>

thighLength = 75.0; // Estimate based on Aluminium prototype
shinWidthClearance = 42.0; // Measured from top of axle shroud to outer surface of shin (with space for m3 washer on axle pin)

module thigh() {
	// TODO - Round off ends with same dieameter as axleshroud 
	translate([(-thighLength / 2) + axleShroudDiameter / 2, 0, axleXOffset]) cube([thighLength, servoWidth + 4 * wallThickness, servoDepth + wallThicknessEitherSide], center=true);
}

thigh();

% rotate([0,90,0]) shin();

