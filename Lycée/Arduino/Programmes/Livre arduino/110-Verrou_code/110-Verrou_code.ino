#include<Servo.h>
Servo myServo;
const int piezo = A0;
const int switchPin = 2;
const int yellowLed = 3;
const int greenLed = 4;
const int redLed = 5;
int knockVal;
int switchVal;
const int quietKnock = 10;
const int loudKnock = 100;
boolean locked = false;
int numberOfKnocks = 0;

void setup() {
  myServo.attach(9);
  pinMode(yellowLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  pinMode(switchPin, INPUT);
  Serial.begin(9600);
  digitalWrite(greenLed, HIGH);
  myServo.write(0);
  Serial.println("La boite est ouverte");
}

void loop() {
  if(locked == false) {
    switchVal = digitalRead(switchPin);

    if(switchVal == HIGH) {
      locked = true;
      digitalWrite(greenLed, LOW);
      digitalWrite(redLed, HIGH);
      myServo.write(90);
      Serial.println("La boite est fermee");
      delay(1000);
    }
  }
  if(locked == true) {
    knockVal = analogRead(piezo);

    if(numberOfKnocks < 3 &&knockVal > 0) {

      if(checkForKnock(knockVal) == true) {
        numberOfKnocks++;
      }
      Serial.print(3-numberOfKnocks);
      Serial.println("coups restants");
    }
    if(numberOfKnocks >= 3) {
      locked = false;
      myServo.write(0);
      delay(20);
      digitalWrite(greenLed, HIGH);
      digitalWrite(redLed, LOW);
      Serial.println("La boite est ouverte !");
    }
  }
}
boolean checkForKnock(int valvue) {
  if (valvue > quietKnock && valvue < loudKnock) {
    digitalWrite(yellowLed, LOW);
    delay(50);
    Serial.print("Coup valide de valeur");
    Serial.println(valvue);
    return true;
  }
  else {
    Serial.print("Mauvaise valeur de coup");
    Serial.println(valvue);
    return false;
  }
}

