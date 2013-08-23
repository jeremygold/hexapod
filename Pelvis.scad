include <MiniServo.scad>
include <Shin.scad> // TODO - Only needed for wallthickness at this stage
include <utils.scad>

// TODO - HexapodDimensions.scad file for all top level dimensions?


pelvisDepth = servoDepth * 2 - differencePadding;
pelvisWidth = servoWidth + wallThicknessEitherSide - differencePadding; 
pelvisHeight = servoWidth + wallThicknessEitherSide - differencePadding;

mountingBlockWidth = wallThicknessEitherSide + mountingTabHeight;
mountingBlockHeight = (mountingTabWidth - servoWidth) / 2;
mountingBlockDepth = servoDepth;

servoAlignmentOffset = (servoWidth - servoHeight) / 2;

module pelvis() {
	difference() {
	  union() {
			cube([pelvisWidth, pelvisHeight, pelvisDepth], center=true);
			mountingBlocks();
			rotate([0,180,90]) mountingBlocks();
		}

		cutouts();
		rotate([0,180,90]) cutouts();
		
	}

	// TODO - Cutouts for M3 nuts next to bolt holes
}

module cutouts() {
	union() {
		cutoutPelvisCenter();
		cutoutAxleShroud();
		cutoutServoMountingWings();
		cutoutBoltHoles();
		cutoutAxleExtensionHole();
	}
}

module cutoutAxleExtensionHole() {
	translate([-axleXOffset, -(servoHeight / 2) + servoAlignmentOffset, -servoDepth / 2]){
		rotate([90,0,0]) {
			m3CskBolt(8);
		}
	}
}

module cutoutBoltHoles() {
		translate([0,0,-servoDepth / 2]) 
			mountingBoltHoles(mountingBlockWidth + differencePadding * 2, servoWidth / 2 - mountingBlockWidth / 2 + wallThickness, m3Radius);
}

module cutoutServoMountingWings() {
	translate([-(servoHeight / 2), 0, servoDepth / 2]) 
		cube([mountingTabHeight + innerSizeTolerance, 
				  mountingTabWidth + innerSizeTolerance, 
					servoDepth + differencePadding], center=true);
}

module mountingBlocks() {
	for(y=[-1,1]) {
		translate ([
		  -(pelvisWidth / 2 - mountingBlockWidth / 2), 
			y * (pelvisHeight / 2 + mountingBlockHeight / 2), 
			mountingBlockDepth / 2]) 
				cube([mountingBlockWidth, mountingBlockHeight, servoDepth], center=true);
	}
}

module cutoutPelvisCenter() {
	union() {
		translate([-servoAlignmentOffset,0,servoDepth / 2])
			cube([servoHeight + innerSizeTolerance, 
					servoWidth + innerSizeTolerance, 
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

% stackedServos();



