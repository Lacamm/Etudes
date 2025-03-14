CXX=g++
CXXFLAGS=-I include


bin/main: obj/main.o obj/mesh.o
	$(CXX) -o $@ $^

obj/main.o: src/main.cpp include/vec3.hpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

obj/mesh.o: src/mesh.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

.PHONY: clean run

run: bin/main
	./bin/main

clean:
	rm -rf bin/* obj/*
