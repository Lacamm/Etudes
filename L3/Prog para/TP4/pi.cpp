#include <mpi.h>
#include <iostream>

using namespace std;

double fx(double x)
{
  double res =(double)4.0/(1+x*x);
  return res;
}


int main ( int argc , char **argv )
{
  int pid, nprocs;  
  MPI_Init (&argc , &argv) ;
  MPI_Comm_rank(MPI_COMM_WORLD, &pid ) ;
  MPI_Comm_size (MPI_COMM_WORLD, &nprocs ) ;
  
  int n = atoi(argv[1]);
  int root = atoi(argv[2]);  
  
  double Pi;  
 
  // A compléter
  double myip, pi, step, sum, x;
  step = 1.0/double(n);
  sum = 0.0;

  for (int i=pid; i<nprocs; i=i+nprocs){
    x = ((double) i + 0.5) * step;
    sum = sum + fx(x);
  }

  myip =sum*step;
  MPI_Reduce(&myip, &Pi, 1, MPI_DOUBLE, MPI_SUM, root,MPI_COMM_WORLD);  
  
  if (pid==root) {
    cout << "PI=" << Pi << endl; //setprecision (15) <<
  }
  MPI_Finalize() ;
  return 0 ;
}
