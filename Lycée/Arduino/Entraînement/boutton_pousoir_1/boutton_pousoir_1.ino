long portPushButton = 2;
long portLED        = 13;
long etatPushButton = HIGH;
void setup() {
  // put your setup code here, to run once:
pinMode (portPushButton, INPUT);
pinMode (portLED,OUTPUT);
}
void loop() {
  // put your main code here, to run repeatedly:
etatPushButton = digitalRead( portPushButton);
  
if (etatPushButton == HIGH)
  {digitalWrite(portLED, HIGH);
  }
 else {digitalWrite(portLED, LOW);}
}
