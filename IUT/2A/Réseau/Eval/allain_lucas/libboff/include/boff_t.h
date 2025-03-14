#ifndef BOFF
#define BOFF
#include <inttypes.h>

typedef struct
{
	uint32_t nbpoints ;
	uint32_t nbtriangles ;
	float * points ;
	uint32_t * indices ;
} 
boff_t;

#endif