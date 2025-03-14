conversion = str(input("Celsius ou Fahrenheit? ")) #Entrer un mot pour choisir quelle conversion faire

while conversion != "Celsius" and conversion != "Fahrenheit": #Tant que les bons mots ne sont sont pas entrés
      conversion = str(input("Celsius ou Fahrenheit? "))#Entrer un mot pour choisir quelle conversion faire

if conversion == "Celsius": #Si le mot entré est "Celsius"
    température_celsius = float(input("Veuillez entrer une température en degrés Celsius= ")) #Saisir une température en degré Celsius
    température_fahrenheit = (température_celsius*1.8)+32 #Conversion en degré Fahrenheit
    print("Température en degré Fahrenheit=", température_fahrenheit) #Affichage de la conversion en degré Fahrenhei

else :
    température_fahrenheit = float(input("Veuillez entrer une température en degrés Fahrenheit= ")) #Saisir une température en degré Fahrenheit
    température_celsius = round((température_fahrenheit-32)/1.8,2) #Conversion en degré Celsius
    print("Température en degré Celsius=", température_celsius) #Affichage de la conversion en degré Celsius

