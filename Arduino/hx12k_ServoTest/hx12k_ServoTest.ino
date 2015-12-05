#include <Servo.h>

Servo pitch_servo;
Servo shin_servo;
Servo hip_servo;

int pos = 0;    
int min_pos = 100;
int max_pos = 180;
int front_pos = 30;
int back_pos = 120;

int delay_ms = 5;
int shin_offset = 00;

void setup() {
  shin_servo.attach(9);
  pitch_servo.attach(10);
  hip_servo.attach(11);  
}

void moveUp() {
  for (pos = min_pos; pos <= max_pos; pos += 1) { 
    pitch_servo.write(pos);             
    shin_servo.write(pos+shin_offset);
    delay(delay_ms);                       
  }
}

void moveDown() {
  for (pos = max_pos; pos >= min_pos; pos -= 1) { 
    pitch_servo.write(pos);              
    shin_servo.write(pos+shin_offset);
    delay(delay_ms);                       
  }
}

void moveForward() {
  for (pos = front_pos; pos <= back_pos; pos += 1) { 
    hip_servo.write(pos);             
    delay(delay_ms);                       
  }
}

void moveBack() {
  for (pos = back_pos; pos >= front_pos; pos -= 1) { 
    hip_servo.write(pos);             
    delay(delay_ms);                       
  }
}

void loop() {
  moveUp();
  moveForward();
  moveDown();
  moveBack();
}
