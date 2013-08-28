include <MiniServo.scad>
include <Shin.scad> // TODO - Only needed for wallthickness at this stage
include <utils.scad>
// TODO - HexapodDimensions.scad file for all top level dimensions?

pelvisDepth = servoDepth * 2 - differencePadding;
pelvisWidth = servoHeight + wallThicknessEitherSide - differencePadding; 
pelvisHeight = servoWidth + wallThicknessEitherSide - differencePadding;

mountingBlockWidth = wallThicknessEitherSide + mountingTabHeight;
mountingBlockHeight = (mountingTabWidth - servoWidth) / 2;
mountingBlockDepth = servoDepth;

wireHoleWidth = 4.0;
wireYOffset = 2.5;

servoAlignmentOffset = (servoWidth - servoHeight) / 2;

// 6.1 is outer diameter of a 5.5mm driver M3 nut
m3NutRadius = 6.1 / 2;
m3NutHeight = 2.0 + innerSizeTolerance; 

module pelvis() {
	union() {
		servoHolder();
		rotate([0,180,90]) servoHolder();
	}
}

module servoHolder() {
	difference() {
	  union() {
			translate([-wallThickness / 2, 0, pelvisDepth / 4]) 
				cube([pelvisWidth, pelvisHeight, pelvisDepth / 2], center=true);
			mountingBlocks();
		}
		cutouts();
	}
}

module cutouts() {
	rotate([0, 180, 90]) {
		union() {
			cutoutPelvisCenter();
			cutoutAxleShroud();
			cutoutServoMountingWings();
			cutoutBoltHoles();
			cutoutAxleExtensionHole();
			cutoutWireEscape();
		}
	}
}

module cutoutWireEscape() {
	translate([-pelvisWidth / 2, -wireYOffset, -servoDepth * 2 / 3])
		cube([wallThickness + differencePadding, wireHoleWidth, servoDepth * 2 / 3], center=true);
}

module mountingBlocks() {
	for(y=[-1,1]) {
		translate ([
		  -(pelvisWidth / 2 - mountingBlockWidth / 2 + wallThickness / 2), 
			y * (pelvisHeight / 2 + mountingBlockHeight / 2), 
			mountingBlockDepth / 2]) 
				cube([mountingBlockWidth, mountingBlockHeight, servoDepth], center=true);
	}
}

module cutoutAxleExtensionHole() {
	translate([-axleXOffset, -(servoHeight / 2) + servoAlignmentOffset, -servoDepth / 2]){
		rotate([90,0,0]) {
			m3CskBolt(8);
		}
	}
}

module mountingBoltHolesWithNuts(height, yOffset, radius) {
	for(x = [-mhX, mhX]) {
		for(z = [-mhY, mhY]) {
			translate([x, yOffset, z]) {
					// Actual mounting hole
					rotate([90,0,0]) cylinder(height, r=radius, center=true);
					translate([0, -(height + m3NutHeight) / 2, 0]) rotate([90,0,0]) cylinder(m3NutHeight, r=m3NutRadius, center=true, $fn=6);
			}
		}
	}
}

module cutoutBoltHoles() {
		translate([0,0,-servoDepth / 2]) 
			mountingBoltHolesWithNuts(mountingBlockWidth + differencePadding * 2, servoWidth / 2 - mountingBlockWidth / 2 + wallThickness, m3Radius);
}

module cutoutServoMountingWings() {
	translate([0, (servoHeight / 2), -servoDepth / 2]) 
		cube([mountingTabWidth + innerSizeTolerance, 
				  mountingTabHeight + innerSizeTolerance, 
					servoDepth + differencePadding], center=true);
}

module cutoutPelvisCenter() {
	union() {
		translate([0, servoAlignmentOffset, -servoDepth / 2])
			cube([servoWidth + innerSizeTolerance, 
					servoHeight + innerSizeTolerance, 
					servoDepth + differencePadding], center=true);
	}
}

module cutoutAxleShroud() {
	hull() {
		translate([0, 0, -servoDepth / 2]) axleAndGearShroud(wallThickness + differencePadding * 2, servoWidth / 2 - differencePadding);
		translate([0, 0, -servoDepth]) axleAndGearShroud(wallThickness + differencePadding * 2, servoWidth / 2 - differencePadding);
	}
}

module stackedServos() {
	union () {
		translate([0, servoAlignmentOffset, -servoDepth / 2]) MiniServo();
		translate([-servoAlignmentOffset, 0, servoDepth / 2]) rotate([0,180,90]) MiniServo();
	}
}

pelvis();

// % stackedServos();



