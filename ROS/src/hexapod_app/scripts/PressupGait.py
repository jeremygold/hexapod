from Gait import Gait, LegState

class PressupGait (Gait):
    def __init__(self):
        Gait.__init__(self)
	self.max_vert_angle = 45
	self.min_vert_angle = -45
        self.vel = 1

    def update(self, robot):
        if self.leg_state == LegState.going_up:
            if self.vert_angle < self.max_vert_angle:
                self.vert_angle += self.vel
            else:
                self.leg_state = LegState.going_down;

        elif self.leg_state == LegState.going_down:
            if self.vert_angle > self.min_vert_angle:
                self.vert_angle -= self.vel
            else:
                self.leg_state = LegState.going_up

        else:
            self.leg_state = LegState.going_up;

        robot.left_front.set_leg_pos( self.horiz_angle, self.vert_angle)
        robot.left_mid.set_leg_pos( self.horiz_angle, self.vert_angle)
        robot.left_back.set_leg_pos( self.horiz_angle, self.vert_angle)
        robot.right_front.set_leg_pos( self.horiz_angle, self.vert_angle)
        robot.right_mid.set_leg_pos( self.horiz_angle, self.vert_angle)
        robot.right_back.set_leg_pos( self.horiz_angle, self.vert_angle)

