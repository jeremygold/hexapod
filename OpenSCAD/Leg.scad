include <Shin.scad>
include <Thigh.scad>
include <Hip.scad>

mirror([0,1,0]) rotate([180,0,0]) thigh();
rotate([180,0,0]) translate([axleXOffset,0,0]) shin();
//mirror([0,0,1]) pelvis();
//stackedServos();

