# Variables
CC := gcc
CFLAGS := -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-abi
LDFLAGS:=
EXEC:=executable
EXEC1:=pascal

# les options -Wno-unused-variable -Wno-unused-parameter
# sont recommandées mais non obligatoires

# Cibles, dépendances
#all : $(EXEC) #$(executable)

# déclaration des fichiers objets nécessaires à la création de executable
executable : 	fonctions.o main.o
							#$(CC) -o executable fonctions.o main.o $(CFLAGS)
							$(CC) -o $@ $^ $(CFLAGS)

pascal : pascal.o catalan.o fonctions.o main_ifndef.o
							$(CC) -o $@ $^ $(CFLAGS)


# fonctions.o: 	main.c
# 							#$(cc) -o exemple.o -c exemple.c $(cflags)
# 							$(cc) -o $@ -c $< $(cflags)
#
# main.o: main.c fonctions.h
# 							#$(cc) -o main.o -c main.c $(cflags)
# 							$(cc) -o $@ -c $< $(cflags)

%.o : %.c
							$(CC) -o $@ -c $< $(CFLAGS)


# Autres
run : $(EXEC)
							./$(EXEC)
run1 : $(EXEC1)
							./$(EXEC1)

clean:
							rm -f *.o core

mrproper: clean
							rm -f $(EXEC)
