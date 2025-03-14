void setup() {
//Tester l'affichage dans le moniteur série
Serial.begin(9600);
Serial.println("com réussie");
delay(1000);
}

void loop() {
Serial.println("oh");
delay(2000);
}
