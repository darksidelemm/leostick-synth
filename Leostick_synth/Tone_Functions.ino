#include <TimerOne.h>


void setTone(unsigned int freq){
  if(freq == 0){stopTone(); return;}
  long period = 1000000L/(long)freq;
  Timer1.initialize(period);
  Timer1.attachInterrupt(tone_isr);
}

void stopTone(){
  Timer1.detachInterrupt();
}

int tone_isr_temp = 0;
void tone_isr(){
  tone_isr_temp++;
  if(tone_isr_temp&1) digitalWrite(11, HIGH);
  else digitalWrite(11, LOW);
}
