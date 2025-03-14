#include <iostream>
#include <omp.h>
#include <stdlib.h>
#define cimg_display 0
#define cimg_plugin "fits.h"
#include "CImg.h"
using namespace cimg_library;
using namespace std;

int main(int, char *argv[]) {
  CImg<short> astro(argv[1]);
  CImg<unsigned char> resca(astro.width(), astro.height(), 1, 1, 0);
  short amin = 32767, amax = 0;
  int i,j;
  int iterations = atoi(argv[2]);

  double start = omp_get_wtime();
  
  //int id = omp_get_thread_num();
  //int np = omp_get_num_threads();

  for (int k = 0; k < iterations; k++) {
    ///////////////////// MODIFIER A PARTIR D'ICI UNIQUEMENT /////////////////
    
    //#pragma omp parallel
    //{
    //int i,j; Q11
    //short myamin = 32767, myamax = 0; 
    #pragma omp parallel for private (i,j) reduction(min:amin) reduction(max:amax)
    for (j = 0; j < astro.height(); j++)
      for (i = 0; i < astro.width(); i++) {
      	
        /*myamin = min(myamin, astro(i, j));
        myamax = max(myamax, astro(i, j));*/
        
        amin = min(amin, astro(i, j));
        amax = max(amax, astro(i, j));
      }
    
    /*#pragma omp critical
    amin = min(myamin, amin);
    amax = max(myamax, amax);
    */
    //}
    
    int arange = amax - amin;
    
    //#pragma omp parallel
    //{
    //int i,j; Q11
    #pragma omp parallel for private (i,j) //gere les threads, donc id et np
    for (j = 0; j < astro.height(); j++)
      for (i = 0; i < astro.width(); i++)
        resca(i, j) = (short)(((int)astro(i, j) - amin) * 255 / arange);
    //}
    
    
    ///////////////////// MODIFIER JUSQU'ICI UNIQUEMENT /////////////////////
  }

  double end = omp_get_wtime();
  cout << (end - start) / iterations << endl;
  resca.save_pnm("/tmp/resca.pgm");
  return 0;
}
