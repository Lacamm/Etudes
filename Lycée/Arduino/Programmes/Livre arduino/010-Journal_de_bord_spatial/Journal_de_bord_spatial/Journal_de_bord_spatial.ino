int switchState = 0; // On déclare les entrées et les sorties

void setup() {
pinMode(4,OUTPUT);  // On déclare les entrées et sorties
pinMode(6,OUTPUT);
pinMode(8,OUTPUT);
pinMode(2,INPUT);
}

void loop() {
switchState = digitalRead(2);
if (switchState == LOW){   // Lorsque le bouton n'est pas appuyé
  delay(1000);
  digitalWrite(4,HIGH); // LED verte
  digitalWrite(6, LOW); // LED rouge
  digitalWrite(8, LOW); // LED rouge
}
else{ // Lorsque que l'on appute sur le bouton
  digitalWrite(4,LOW); // LED verte
  digitalWrite(6, LOW); // LED rouge
  digitalWrite(8, HIGH); // LED rouge
  delay(250);  // Faire clignoter les LED pour signifier la fin du processus
  digitalWrite(6, HIGH);
  digitalWrite(8,LOW);
  delay(250);
}
}
