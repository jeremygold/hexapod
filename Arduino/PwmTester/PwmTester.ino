#include <Servo.h>
 
Servo testServo; 
int pos = 0;

const int UP_DOWN_MIN = 70;
const int UP_DOWN_MAX = 130;
const int SPEED_DELAY = 5;

void setup() {
  testServo.attach(11);
}

void loop() {
  testServo.write(90);    
}

void temp() {
  for(pos = UP_DOWN_MIN; pos < UP_DOWN_MAX; pos += 1)  
  {                                 
    testServo.write(pos);    
    delay(SPEED_DELAY);                       
  }
  for(pos = UP_DOWN_MAX; pos>=UP_DOWN_MIN; pos -= 1)     
  {                                
    testServo.write(pos);    
    delay(SPEED_DELAY);                       
  } 
}
