from Gait import Gait, LegState

class CrabRightGait (Gait):
    def __init__(self):
        Gait.__init__(self)
	self.max_vert_angle = 11
	self.min_vert_angle = -11
        self.max_knee_angle = 20
        self.min_knee_angle = -20
        self.knee_angle = 0
        self.vel = 3

    def update(self, robot):
        if self.leg_state == LegState.going_up:
            if self.vert_angle < self.max_vert_angle:
                self.vert_angle += self.vel
            else:
                self.leg_state = LegState.going_forward;

        elif self.leg_state == LegState.going_forward:
            if self.knee_angle < self.max_knee_angle:
                self.knee_angle += self.vel
            else:
                self.leg_state = LegState.going_down

        elif self.leg_state == LegState.going_down:
            if self.vert_angle > self.min_vert_angle:
                self.vert_angle -= self.vel
            else:
                self.leg_state = LegState.going_back

        elif self.leg_state == LegState.going_back:
            if self.knee_angle > self.min_knee_angle:
                self.knee_angle -= self.vel
            else:
                self.leg_state = LegState.going_up

        else:
            self.leg_state = LegState.going_up;

        robot.left_front.set_leg_pos(  0, -self.vert_angle, -self.knee_angle)
        robot.left_mid.set_leg_pos(    0,  self.vert_angle,  self.knee_angle)
        robot.left_back.set_leg_pos(   0, -self.vert_angle, -self.knee_angle)
        robot.right_front.set_leg_pos( 0,  self.vert_angle, -self.knee_angle)
        robot.right_mid.set_leg_pos(   0, -self.vert_angle,  self.knee_angle)
        robot.right_back.set_leg_pos(  0,  self.vert_angle, -self.knee_angle)

