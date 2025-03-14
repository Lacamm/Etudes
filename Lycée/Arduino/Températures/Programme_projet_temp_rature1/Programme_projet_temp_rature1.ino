const int capteurPremier = A0; // On associe un nom au port A0
const int capteurSecond = A1; // On associe un nom au port A1

void setup() {
  Serial.begin(9600); // On se cale sur la vitesse de lecture de l'orinateur
}

void loop() {
  int temperature1 = analogRead(capteurPremier);  //On lit la vleur numérique du capteur 1
  Serial.println("Capteur premier : ");  // On affiche la phrase à la ligne
  Serial.print(temperature1-1005);   // On affiche la valeur de température
  Serial.print("C°");
  Serial.println(""); // On affiche une ligne vide pour que ce soit lisible


  int temperature2 = analogRead(capteurSecond);  //On lit la vleur numérique du capteur 2
  Serial.println("Capteur second : ");  // On affiche la phrase à la ligne
  Serial.print(temperature2-1005);   // On affiche la valeur de température
  Serial.print("C°");
  Serial.println(""); // On affiche une ligne vide pour que ce soit lisible
  Serial.println(""); // On affiche une ligne vide pour que ce soit lisible
  
  delay(1000); // Attendre 1 seconde
}

