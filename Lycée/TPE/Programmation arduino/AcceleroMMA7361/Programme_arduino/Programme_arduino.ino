#include <AcceleroMMA7361.h> // inclure la librairie de l'accéléromètre

AcceleroMMA7361 accelero;
int x;// Création de la variable pour l'accélération

void setup() 
{
 // put your setup code here, to run once
 Serial.begin(9600); // Démarrer la liaison série
 accelero.begin(13, 12, 11, 10, A0, A1, A2); // Démarrer le composant
 accelero.setARefVoltage(5); // Régler la tension de référence
 accelero.setSensitivity(LOW); // Régler la sensibilité du composant +/-6G
 accelero.calibrate(); // Calibrer le composant
}

void loop() 
{
  // put your main code here, to run repeatedly
 x = accelero.getXAccel(); // Lecture de l'axe X
 Serial.print("nx: "); // Afficher la valeur de l'axe X
 Serial.println(x);
 Serial.print(" tG*10^-2");
 delay(500); // Délais pour rendre ça lisible
}
