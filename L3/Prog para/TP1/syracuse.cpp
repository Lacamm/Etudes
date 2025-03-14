#include <iostream>
#include <omp.h>
using namespace std;

#define TOTAL 2000000

int main(int, char *[])
{
    int pass=0;
    double start = omp_get_wtime();
    
    #pragma omp parallel
    {
    
    int cur, mypass=0; // privée
    
    #pragma omp single
    cout << omp_get_num_threads() << endl;
    
    for(int i=omp_get_thread_num(); i<TOTAL; i+=omp_get_num_threads()) {
	cur=i;
	while (cur>1){
	    cur=cur%2?3*cur+1:cur/2;
	}
	mypass ++;
    }
    
    #pragma omp critical
    pass+=mypass;
    
    }    

    double end = omp_get_wtime();
    cout << pass << " out of " << TOTAL << "! (delta=" << TOTAL-pass << ")" << endl;
    cout << "ellapsed time: " << (end-start)*1000 << "ms" << endl;
}
