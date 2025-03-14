#include <stdio.h>
#include <stdlib.h>
#include "readboff.h"
#include "writeboff.h"
#include "boff_t.h"

int main()
{
	boff_t test = readboff("./rabbit.boff");
	printf("%u \n %u \n %f \n %u \n", test.nbpoints, test.nbtriangles, *test.points, *test.indices);

	writeboff("./test.boff",  test);
	return 0;
}
