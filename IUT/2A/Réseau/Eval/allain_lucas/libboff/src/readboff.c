#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include "boff_t.h"

boff_t readboff( const char * const filename)
{
	FILE * fichier = fopen(filename, "r");

 	if (fichier) {
 		unsigned int nbpoints, nbtriangles;
 		float * points;
 		unsigned int * indices;

	    char boff[4];
	    fread(boff, sizeof(char), 4, fichier);
	    fread(&nbpoints, sizeof(int), 1, fichier);
	    fread(&nbtriangles, sizeof(int), 1, fichier);


	    printf("%s\n %u\n %u\n", boff, nbpoints, nbtriangles);

	    points = (float *) malloc(3 * nbpoints * sizeof(float));
	    indices = (unsigned int *) malloc(3 * nbtriangles * sizeof(unsigned int));

	    fread(points, 3*sizeof(float), nbpoints, fichier);
	    fread(indices, 3*sizeof(int), nbtriangles, fichier);

		boff_t object_boff = 
		{
			(uint32_t) nbpoints,
			(uint32_t) nbtriangles,
			points,
			(uint32_t *) indices
		};
		fclose(fichier);
		return object_boff;
	}
}
