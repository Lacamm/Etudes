CXXFLAGS=-I include

bin/test: src/test.cpp include/vec4f.hpp include/mat4x4f.hpp include/transform.hpp include/vec3f.hpp
	g++ -o $@ $< $(CXXFLAGS)

clean:
	rm -rf bin/* obj/*

.PHONY: clean
