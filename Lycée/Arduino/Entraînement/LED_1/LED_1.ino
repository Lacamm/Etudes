void setup() 
{
  // put your setup code here, to run once:
pinMode (7, OUTPUT);//Définir le port de sortie 
}
void loop() {
  // put your main code here, to run repeatedly:
digitalWrite (7, HIGH);// Allumer la LED
delay(1000);//Laisser un délai de 1 seconde
digitalWrite (7, LOW);//Eteindre la LED
delay(1000);//Laisser un délai de 1 seconde
}
