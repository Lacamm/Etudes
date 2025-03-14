#include <mpi.h>
#include <iostream>
#include <iomanip>
#include <random>
#include <math.h>

using namespace std;

int main ( int argc , char **argv )
{
  int pid, nprocs;
  MPI_Init (&argc , &argv) ;
  MPI_Comm_rank(MPI_COMM_WORLD, &pid ) ;
  MPI_Comm_size (MPI_COMM_WORLD, &nprocs ) ;

  int n = atoi(argv[1]);
  int root = atoi(argv[2]);

  int* sendcounts;
  int* displ;
  int n_local = n/nprocs;
  int reste = n%nprocs;
  float *vector;

  if (pid==root) {
    vector = new float[n];
    default_random_engine re(time(0));
    uniform_real_distribution<> distrib {0,10};
    for (size_t i = 0; i < n; i++) {
      vector[i] = distrib(re);
      std::cout << "vecteur initial" << '\n';
    }
    for (size_t i = 0; i < n; i++) {
      std::cout << vector[i] << " " << '\n';
    }
    sendcounts = new int[nprocs];
    displ = new int[nprocs];
    int ptr = 0;
    for (size_t i = 0; i < nprocs; i++) {
      if (i < reste) {
        sendcounts[i] = n_local + 1;
        displ[i] = ptr;
        ptr = ptr + n_local + 1;
      } else {
        sendcounts[i] = n_local;
        displ[i] = ptr;
        ptr = ptr + n_local;
      }
    }
    if(pid<reste) n_local++;
    //Affichage
    for (size_t i = 0; i < nprocs; i++) {
      std::cout << sendcounts[i] << " ";
      std::cout << displ[i] << " " << '\n';
    }
  }

  if (pid<reste) {
    n_local++;

  }
  float* vector_local = new float[n_local];
  MPI_Scatterv(vector, sendcounts, displ, MPI_FLOAT, vector_local, n_local, MPI_FLOAT, root, MPI_COMM_WORLD);

  float scarres = 0;
  for (size_t i = 0; i < n_local; i++) {
    scarres+=vector_local[i]*vector_local[i];
  }

  float ncarres;
  MPI_Allreduce(&scarres, &ncarres, 1, MPI_FLOAT, MPI_SUM, MPI_COMM_WORLD);
  ncarres = sqrt(ncarres);
  for (size_t i = 0; i < n_local; i++) {
    vector_local[i] /= ncarres;
  }
  MPI_Gatherv(vector_local, n_local, MPI_FLOAT, vector, sendcounts, displ, MPI_FLOAT, root, MPI_COMM_WORLD);
  if (pid == root) {
    std::cout << "vecteur normalisé" << '\n';
    for (size_t i = 0; i < n; i++) {
      std::cout << vector[i] << '\n';
    }
  }
  MPI_Finalize() ;
  return 0 ;
}