# compilateur
CC := gcc
# options de compilation
CFLAGS := -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-unused-variable -Wno-unused-parameter
EXEC := executable

# all est la cible choisie par défaut par la commande make
# elle dépend de la règle $(EXEC), qui va être réalisée
# NOTE --- les cibles ne doivent pas avoir le même nom qu'un fichier
all : $(EXEC)

# déclaration des fichiers objets nécessaires à la création de $(EXEC)
# exécutée avec la commande make $(EXEC)
$(EXEC) : fonctions.o main.o
# instructions de compilation
# $@ fait référence à la cible, $^ aux dépendances
	$(CC) $(CFLAGS) -o $@ $^

regle_pascal : fonctions.o catalan.o pascal.o main_ifndef.o
	$(CC) $(CFLAGS) -o $@ $^

# règle générale pour la génération des .o
# $(EXEC) dépend de fonctions.o et main.o, qui seront donc exécutés 
# via cette règle en premier lieu
%.o : %.c
# la génération des fichiers .o dépend de fichiers .c 
# (aucune cible ne correspondant à ces derniers, l'instruction est exécutée)
# $< correspond à chaque dépendance prise les unes à la suite des autres 
	$(CC) $(CFLAGS) -o $@ -c $<

# règle de nettoyage (supprimant les fichiers .o), ne dépendant d'aucune autre règle
clean : 
	rm *.o  $(EXEC)

run : $(EXEC)
	./$(EXEC)
