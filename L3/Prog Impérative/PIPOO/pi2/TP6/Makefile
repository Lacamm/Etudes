# Variables
CC := gcc
CFLAGS := -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-abi
LDFLAGS:=
EXEC:= main

# les options -Wno-unused-variable -Wno-unused-parameter
# sont recommandées mais non obligatoires

# Cibles, dépendances
#all : $(EXEC)

# déclaration des fichiers objets nécessaires à la création de executable

# A chaque nouvel executable, refaire le bloc ci-dessous
main : fonction.o chemin.o main.o
							$(CC) -o $@ $^ $(CFLAGS)


%.o : %.c
							$(CC) -o $@ -c $< $(CFLAGS)

# Autres
run : $(EXEC)
							./$(EXEC)

clean:
							rm -f *.o core

mrproper: clean
							rm -f $(EXEC)

mem: $(EXEC)
							valgrind --leak-check=full ./$(EXEC)
