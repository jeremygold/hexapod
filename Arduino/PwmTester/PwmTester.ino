#include <Servo.h>
 
Servo testServo; 
int pos = 0;

const int CENTER_POS = 90;
const int MOVE_ANGLE = 90;
const int MOVE_MIN = CENTER_POS - (MOVE_ANGLE / 2);
const int MOVE_MAX = CENTER_POS + (MOVE_ANGLE / 2);
const int SPEED_DELAY = 5;

const int PULLUP_PIN = 8; // Using this pin to generate 5V to pullup when switch is pressed
const int INPUT_PIN = 10;
const int SERVO_PIN = 11;

void setup() {
  testServo.attach(SERVO_PIN);

  pinMode(PULLUP_PIN, OUTPUT);
  digitalWrite(PULLUP_PIN, HIGH);

  pinMode(INPUT_PIN, INPUT);
}

void moveServo() {
  for(pos = CENTER_POS; pos <= MOVE_MAX; pos += 1)  
  {                                 
    testServo.write(pos);    
    delay(SPEED_DELAY);                       
  }
  delay(500);

  for(pos = MOVE_MAX; pos >= MOVE_MIN; pos -= 1)     
  {                                
    testServo.write(pos);    
    delay(SPEED_DELAY);                       
  } 
  delay(500);


  for(pos = MOVE_MIN; pos <= CENTER_POS; pos += 1)  
  {                                 
    testServo.write(pos);    
    delay(SPEED_DELAY);                       
  }
}

void loop() {
  testServo.write(CENTER_POS);    
  
  while(digitalRead(INPUT_PIN) == LOW) { 
    delay(10);
  }

  moveServo();
}


