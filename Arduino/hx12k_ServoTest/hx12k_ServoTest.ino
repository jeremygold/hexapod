#include <Servo.h>

Servo mid_left_pitch_servo;
Servo mid_left_shin_servo;
Servo mid_left_hip_servo;
Servo front_left_pitch_servo;
Servo front_left_shin_servo;
Servo front_left_hip_servo;

Servo centered_servo;

int pos = 0;    
int min_pos = 100;
int max_pos = 180;
int front_pos = 30;
int back_pos = 120;
int front_hip_offset = 50;

int servo_step = 2;
int delay_ms = 10;
int shin_offset = 00;
int front_shin_offset = -50;
int front_pitch_offset = -50;

void setup() {
  mid_left_shin_servo.attach(9);
  mid_left_pitch_servo.attach(10);
  mid_left_hip_servo.attach(11);  

  //front_left_shin_servo.attach(3);
  front_left_pitch_servo.attach(5);
  front_left_hip_servo.attach(6);  
  
  centered_servo.attach(3);
}

void moveUp() {
  for (pos = min_pos; pos <= max_pos; pos += servo_step) { 
    mid_left_pitch_servo.write(pos);             
    mid_left_shin_servo.write(pos+shin_offset);

    front_left_pitch_servo.write(max_pos - (pos + front_pitch_offset));
    front_left_shin_servo.write(max_pos - (pos + front_shin_offset));
    delay(delay_ms);                       
  }
}

void moveDown() {
  for (pos = max_pos; pos >= min_pos; pos -= servo_step) { 
    mid_left_pitch_servo.write(pos);              
    mid_left_shin_servo.write(pos+shin_offset);

    front_left_pitch_servo.write(max_pos - (pos + front_pitch_offset));              
    front_left_shin_servo.write(max_pos - (pos + front_shin_offset));
    delay(delay_ms);                       
  }
}

void moveForward() {
  for (pos = front_pos; pos <= back_pos; pos += servo_step) { 
    mid_left_hip_servo.write(pos);             
    front_left_hip_servo.write(back_pos - pos + front_hip_offset);             
    delay(delay_ms);                       
  }
}

void moveBack() {
  for (pos = back_pos; pos >= front_pos; pos -= servo_step) { 
    mid_left_hip_servo.write(pos);             
    front_left_hip_servo.write(back_pos - pos + front_hip_offset);             
    delay(delay_ms);                       
  }
}

void loop() {
  centered_servo.write(90);
  delay(1000);
  
  //centered_servo.write(0);
  //delay(1000);

  //centered_servo.write(180);
  //delay(1000);
  //moveUp();
  //moveForward();
  //moveDown();
  //moveBack();
}
