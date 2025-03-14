const int valeurCapteur = A0;
float temperature = 0;
float tension = 0;
float valeur = 0;

void setup() {
  Serial.begin(9600);
  pinMode(valeurCapteur, OUTPUT);
  analogWrite(valeurCapteur, LOW);
}

void loop() {
  temperature = analogRead(valeurCapteur);
  Serial.print("Température: ");
  Serial.println(temperature);
  delay(1000);
}
