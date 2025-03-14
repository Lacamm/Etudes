const int sensorPin = A0;
const float baselineTemp = 22.0;

void setup() {
  Serial.begin(9600); // On se cale sur la vitesse de lecture de l'orinateur
    for(int pinNumber = 2; pinNumber < 5; pinNumber++){  // On utilise une boucle for qui va permettre de déclarer beaucoup de port digitaux comme sortie et de les mettre à un niveau bas
                                                         // On incrémente cette boucle de 1
    pinMode(pinNumber, OUTPUT);
    digitalWrite(pinNumber, LOW);
    }
}

void loop() {
  int sensorVal = analogRead(sensorPin);  //On lit la vleur numérique du capteur
  Serial.print("Valeur capteur: ");  // On l'affiche
  Serial.print(sensorVal);
  
  float voltage = (sensorVal/1024.0)*5.0;  //On transforme la valeur du capteur en tension
  Serial.print(", Volts: ");  // On l'affiche
  Serial.print(voltage);

  float temperature = (voltage - .5)*100;  //On transforme la valeur de tension en température
  Serial.print(", Degrés C°: ");  // On l'affiche
  Serial.print('\n');

  if(temperature < baselineTemp){  // On allume une à une les LED en fonction de la valeur de température
    digitalWrite(2,LOW);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
  }else if(temperature >= baselineTemp+2 && temperature < baselineTemp+4){
    digitalWrite(2,HIGH);
    digitalWrite(4,LOW);
    digitalWrite(6,LOW);
  }else if(temperature >= baselineTemp+4 && temperature < baselineTemp+6){
    digitalWrite(2,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(6,LOW);
  }else if(temperature >= baselineTemp+6){
    digitalWrite(2,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(6,HIGH);
  }
  delay(1000);
}
