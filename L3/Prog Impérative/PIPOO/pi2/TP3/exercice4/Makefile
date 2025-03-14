# Variables
CC := gcc
CFLAGS := -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-abi
LDFLAGS:=
EXEC:=exo4

# -lm pout math.h

# Cibles, dépendances
all : $(EXEC)

exo4 : exo4.o
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
