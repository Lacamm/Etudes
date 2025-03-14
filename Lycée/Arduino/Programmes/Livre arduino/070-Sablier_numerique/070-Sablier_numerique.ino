const int switchPin = 13;
unsigned long previousTime = 0;
int switchState = 0;
int prevSwitchState = 0;
int led = 2;
long interval = 600000;

void setup() {
  for(int x = 2; x < 13; x+2){
    pinMode(x, OUTPUT);
    }
  pinMode(switchPin, INPUT);
  }

void loop() {
  unsigned long currentTime = millis();
  if (currentTime - previousTime > interval){
    previousTime = currentTime;
    digitalWrite(led, HIGH);
    led+2;

    if (led == 12){      
    }
  }
  switchState = digitalRead(switchPin);
  
  if (switchState != prevSwitchState){
    for(int x = 2; x < 13; x+2){
      digitalWrite(x, LOW);
    }
    led = 2;
    previousTime = currentTime;
  }
  prevSwitchState = switchState;
}
