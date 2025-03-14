from Espece import *

abeille = Espece("abeille",Espece.lireFichier("abeille.adn"))
eponge = Espece("eponge", Espece.lireFichier("eponge.adn"))
lapin = Espece("lapin", Espece.lireFichier("lapin.adn"))
humain = Espece("humain", Espece.lireFichier("humain.adn"))
roadrunner = Espece("roadrunner", Espece.lireFichier("roadrunner.adn"))
trex = Espece("trex", Espece.lireFichier("trex.adn"))


print("éponge et abeille: ",Espece.mutations(abeille,eponge))
print("lapin et abeille: ",Espece.mutations(abeille,lapin))