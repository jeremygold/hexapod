#include <Servo.h>
 
Servo elbow_RF; 
Servo shoulderV_RF;
Servo shoulderH_RF;

Servo elbow_LF;
Servo shoulderV_LF;
Servo shoulderH_LF;
 
int pos = 0;
int speed_delay=50;

const int GAIT_PAUSE = 200;

const int UP_DOWN_MIN = 70;
const int UP_DOWN_MAX = 130;
const int FWD_BACK_MIN = 50;
const int FWD_BACK_MAX = 110;
 
void setup()
{
  shoulderH_RF.attach(3);
  shoulderV_RF.attach(5);
  elbow_RF.attach(6);

  shoulderH_LF.attach(9);
  shoulderV_LF.attach(10);
  elbow_LF.attach(11);
} 

void moveRF(int up_down_pos, int fwd_back_pos) {
  moveLeg(elbow_RF, shoulderV_RF, shoulderH_RF, up_down_pos, fwd_back_pos);
}

void moveLF(int up_down_pos, int fwd_back_pos) {
  moveLeg(elbow_LF, shoulderV_LF, shoulderH_LF, UP_DOWN_MAX-(up_down_pos-UP_DOWN_MIN), FWD_BACK_MAX-(fwd_back_pos-FWD_BACK_MIN));
}

void moveLeg(Servo elbow, Servo shoulderV, Servo shoulderH, int up_down_pos, int fwd_back_pos) {
  elbow.write(up_down_pos-20);
  shoulderV.write(up_down_pos);
  shoulderH.write(fwd_back_pos);
}

void legUpDown(Servo elbow, Servo shoulderV) {
  for(pos = UP_DOWN_MIN; pos < UP_DOWN_MAX; pos += 1)  
  {                                 
    elbow.write(pos - 20); 
    shoulderV.write(pos);    
    delay(speed_delay);                       
  }
  for(pos = UP_DOWN_MAX; pos>=UP_DOWN_MIN; pos-=1)     
  {                                
    elbow.write(pos - 20);              
    shoulderV.write(pos);    
    delay(speed_delay);                       
  } 
}

void legForwardBack(Servo shoulderH) {
  for(pos = FWD_BACK_MIN; pos < FWD_BACK_MAX; pos += 1)  
  {                                 
    shoulderH.write(pos);    
    delay(speed_delay);                       
  }
  for(pos = FWD_BACK_MAX; pos>=FWD_BACK_MIN; pos-=1)     
  {                                
    shoulderH.write(pos);    
    delay(speed_delay);                       
  } 
}

void loop() {
  moveLF(UP_DOWN_MIN, FWD_BACK_MIN);
  moveRF(UP_DOWN_MAX, FWD_BACK_MAX);
  delay(GAIT_PAUSE);
  
  moveLF(UP_DOWN_MIN, FWD_BACK_MAX);
  moveRF(UP_DOWN_MAX, FWD_BACK_MIN);
  delay(GAIT_PAUSE);
  
  moveLF(UP_DOWN_MAX, FWD_BACK_MAX);
  moveRF(UP_DOWN_MIN, FWD_BACK_MIN);
  delay(GAIT_PAUSE);
  
  moveLF(UP_DOWN_MAX, FWD_BACK_MIN);
  moveRF(UP_DOWN_MIN, FWD_BACK_MAX);
  delay(GAIT_PAUSE);
  
   //legUpDown(elbow_RF, shoulderV_RF);
   //legUpDown(elbow_LF, shoulderV_LF);
   //legForwardBack(shoulderH_RF);
   //legForwardBack(shoulderH_LF);
}
  
