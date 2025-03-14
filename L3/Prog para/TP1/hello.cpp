#include <iostream>
#include <omp.h>
using namespace std;

int main(int, char *[])
{  
    #pragma omp parallel
    {
    omp_set_num_threads(32);
    
    int id = omp_get_thread_num();
    int np = omp_get_num_threads();
    
    	#pragma omp critical
    	cout << "Bonjour(" << id << "/" << np << ")" << endl;
    	
    	#pragma omp barrier
    	#pragma omp single
    	#pragma omp critical
    	cout << "Nous sommes " << np << " threads dans cette équipe" << endl;
    	
    	#pragma omp barrier
    	#pragma omp critical
    	cout << "Au revoir(" << id << "/" << np << ")"<< endl;
    }
}
