# compilateur
CC := gcc
# options de compilation
CFLAGS := -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-unused-variable -Wno-unused-parameter

# règle de compilation --- exécutables
all : vigenere #exo2 #main

vigenere : exo3.o fonction.o #crypto.o main.o
	$(CC) $(CFLAGS) -o $@ $^

exo2 : exo2.o fonction.o
	$(CC) $(CFLAGS) -o $@ $^

main : main.o fonction.o
	$(CC) $(CFLAGS) -o $@ $^


%.o: %.c
	$(CC) $(CFLAGS) -o $@ -c $<

# options de compilation

run : vigenere
	./vigenere

runmain : main
	./main

runexo2 : exo2
	./exo2


memoire : vigenere
	valgrind --leak-check=full ./vigenere

memoiremain : main
	valgrind --leak-check=full ./main

memoireexo2 : exo2
	valgrind --leak-check=full ./exo2

clean:
	rm *.o vigenere
