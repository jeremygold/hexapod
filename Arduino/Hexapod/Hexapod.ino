mkdir Arduino#include <Servo.h>
 
Servo elbow; 
Servo shoulderV;
Servo shoulderH;
 
int pos = 0;

 
void setup()
{
  shoulderH.attach(0);
  shoulderV.attach(1);
  elbow.attach(2);  
} 

void legUpDown() {
  for(pos = 50; pos < 130; pos += 1)  
  {                                 
    elbow.write(pos - 20); 
    shoulderV.write(pos);    
    delay(5);                       
  }
  for(pos = 130; pos>=50; pos-=1)     
  {                                
    elbow.write(pos - 20);              
    shoulderV.write(pos);    
    delay(5);                       
  } 
}

void legForwardBack() {
  for(pos = 70; pos < 110; pos += 1)  
  {                                 
    shoulderH.write(pos);    
    delay(5);                       
  }
  for(pos = 110; pos>=70; pos-=1)     
  {                                
    shoulderH.write(pos);    
    delay(5);                       
  } 
  
}

void loop() {
   legUpDown();
   legForwardBack();
}
  
