m3Radius = 3.0/2;
m3CskTopRadius = 6.0/2;
m3CskHeadHeight = 2.0;
m8Radius = 8.0/2;

// TODO - This should take a vector, and a "center" option so it can be easily re-used
module roundedCube(_x,_y,_z,_r) {
	hull() {
		for(xPos = [-(_x/2-_r),(_x/2-_r)]) {
			for(yPos = [-(_y/2-_r),(_y/2-_r)]) {
				translate([xPos, yPos, -_z/2]) cylinder(h=_z,r=_r);
			}
		}
	}
}

// TODO - Test that this results in correctly sized bolt
module m3CskBolt(length) {
	# union() {
	// Countersunk section // TODO - how tall is the countersunk section
		translate([0,0,m3CskHeadHeight / 2]) cylinder(h=m3CskHeadHeight, r1=m3CskTopRadius, r2=m3Radius, center=true);
		translate([0,0,m3CskHeadHeight / 2 + length / 2]) cylinder(h=length, r=m3Radius, center=true);
	}
}


