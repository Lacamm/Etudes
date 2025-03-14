# Variables
CC := gcc
CFLAGS := -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-abi
LDFLAGS:=
EXEC:= exercice2 #jump #exercice1

# les options -Wno-unused-variable -Wno-unused-parameter
# sont recommandées mais non obligatoires

# Cibles, dépendances
#all : $(EXEC)

# déclaration des fichiers objets nécessaires à la création de executable

# A chaque nouvel executable, refaire le bloc ci-dessous
# exercice1 : fonction.o exercice1.o
# 							$(CC) -o $@ $^ $(CFLAGS)
#
# jump: jump.o
# 							$(CC) -o $@ $^ $(CFLAGS)

exercice2 : fonction.o exercice2.o
							$(CC) -o $@ $^ $(CFLAGS)

# exercice3 : fonction.o exercice3.o
# 							$(CC) -o $@ $^ $(CFLAGS)

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
