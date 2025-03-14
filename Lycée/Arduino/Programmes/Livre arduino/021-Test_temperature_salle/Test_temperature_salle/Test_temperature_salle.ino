const int sensorPin = A0; // Simplification pour d'éventuels changements

void setup() {
  Serial.begin(9600); // On se cale sur la vitesse de lecture de l'arduino
}

void loop() {
  int sensorVal = analogRead(sensorPin);  //On lit la valeur numérique du capteur
  Serial.print("Valeur capteur: ");
  Serial.print(sensorVal);

  float voltage = (sensorVal/1024.0)*5.0; // On transforme la valeur du capteur en une tension
  Serial.print(", Volts: ");
  Serial.print(voltage);

  float temperature = (voltage - .5)*100; // On transforme la valeur de la tension en température
  Serial.print(", Degrés C°: ");
  Serial.print(temperature);
  Serial.print('\n'); // retour ligne
  delay(1000);
}
