const int greenLEDPin = 6; // On définit les port digitaux de le LED
const int redLEDPin = 9;
const int blueLEDPin = 11;

const int greenSensorPin = A0; // On définit les ports analog des photorésistances
const int redSensorPin = A2;
const int blueSensorPin = A4;

int redValvue = 0; // On définitles valeurs que la LED devra suivre
int greenValvue = 0;
int blueValvue = 0;

int redSensorValvue = 0; // On définit les valeurs à lire des photorésistances
int greenSensorValvue = 0;
int blueSensorValvue = 0;

void setup() {
  Serial.begin(9600); // On se cale sur la vitesse de lecture de l'ordinateur

  pinMode(greenLEDPin, OUTPUT);  // On définit les prots de la LED comme des sorties
  pinMode(redLEDPin, OUTPUT);
  pinMode(blueLEDPin, OUTPUT);
}

void loop() {
  greenSensorValvue = analogRead(greenSensorPin);  // On lit les valeurs des photorésistances
  delay(5);
  redSensorValvue = analogRead(redSensorPin);
  delay(5);
  blueSensorValvue = analogRead(blueSensorPin);

  Serial.print("Raw Sensor Valvue \n \t Red: ");  // On affiche les valeurs des photorésistances
  Serial.print(redSensorValvue);
  Serial.print("\n \t Green: ");
  Serial.print(greenSensorValvue);
  Serial.print("\n \t Blue: ");
  Serial.print(blueSensorValvue);

  redValvue = redSensorValvue/4;  // On calcule les valeurs "d'intensités" lumineuses que la LED va adopter
  blueValvue = blueSensorValvue/4;
  greenValvue = greenSensorValvue/4;

  Serial.print("Valeurs recalculees \n \t Red: "); // On affiche les valeurs
  Serial.print(redValvue);
  Serial.print("\n \t Green: ");
  Serial.print(greenValvue);
  Serial.print("\n \t Blue: ");
  Serial.print(blueValvue);

  analogWrite(redLEDPin, redValvue);  // On allume la LED suivant les différentes valeurs des photorésistances
  analogWrite(greenLEDPin, greenValvue);
  analogWrite(blueLEDPin, blueValvue);
}
