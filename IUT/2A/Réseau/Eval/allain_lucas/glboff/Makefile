CFLAGS=-I include
LDLIBS= -lGL -lGLU -lglut -lm
BIN=bin/main
SRCS=$(wildcard src/*.c)
OBJS=$(SRCS:src/%.c=obj/%.o)

all: $(BIN)

${BIN}: ${OBJS}
	${CC} -o $@ $^ $(LDLIBS)

obj/%.o: src/%.c
	${CC} -c -o $@ $< $(CFLAGS)

obj/%.o: src/%.c include/%.h
	${CC} -c -o $@ $< $(CFLAGS)

run: $(BIN)
	./$<

clean:
	rm -f obj/* bin/*

.PHONY: clean all run