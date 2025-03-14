#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include "boff_t.h"


void writeboff(const char * const filename, boff_t b)
{
	FILE * fichier = fopen(filename, "w");

	if (fichier) {
		char boff[4] = {'B', 'O', 'F', 'F'};
		fwrite((const void *) boff, sizeof(char), 4, fichier);
		fflush(fichier);
		fwrite((const void *) b.nbpoints, sizeof(uint32_t), 1, fichier);
		fwrite((const void *) b.nbtriangles, sizeof(uint32_t), 1, fichier);

	}

	fclose(fichier);
}