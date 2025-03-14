const int Voie_0=0;//Déclaration constante entière de la broche analogique A0 en Voie 0=0
float mesure_brute=0;//Déclaration variable décimale "mesure_brute=0", pour afficher les résultats de la mesure

void setup() {
Serial.begin(9600);//Définir la vitesse de transmission des valeurs de l'arduino vers le moniteur série à 9600 bits par seconde
}
void loop() {
mesure_brute=analogRead(Voie_0);//Lire la valeur de Voie 0
Serial.println(mesure_brute-328);//Afficher la valeur de mesure_brute,on lui soustrait 328
delay(500);//Laisser un délai de 0.5 seconde
}
