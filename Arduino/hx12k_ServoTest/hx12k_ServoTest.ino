#include <Servo.h>

Servo pitch_servo;
Servo shin_servo;

int pos = 0;    
int min_pos = 30;
int max_pos = 110;
int delay_ms = 20;
int shin_offset = 70;

void setup() {
  pitch_servo.attach(6);  
  shin_servo.attach(5);
}

void loop() {
  for (pos = min_pos; pos <= max_pos; pos += 1) { 
    // in steps of 1 degree
    pitch_servo.write(pos);             
    shin_servo.write(pos+shin_offset);
    delay(delay_ms);                       
  }
  for (pos = max_pos; pos >= min_pos; pos -= 1) { 
    pitch_servo.write(pos);              
    shin_servo.write(pos+shin_offset);
    delay(delay_ms);                       
  }
}
