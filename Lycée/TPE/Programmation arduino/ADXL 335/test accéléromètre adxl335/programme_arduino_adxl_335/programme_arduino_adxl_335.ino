#include <ADXL335.h>;//Inclure la bibliothèque de l'accéléromètre
//Initialiser le port A0 à 0

void setup() 
{
Serial.begin(9600); //Définir la vitesse de transmission des valeurs de l'arduino vers le moniteur série à 9600 bits par seconde
pinMode(A0,OUTPUT);//Déclarer le port analogique A0 en sorie
//Démarrer le capteur
}

void loop() 
{
/*
*/
Serial.print(analogRead=A0);//Lire la valeur du port A0
Serial.println("x=  ");//Afficher "X=  "
delay(500);//Laisser un délai de 0.5 seconde
}
