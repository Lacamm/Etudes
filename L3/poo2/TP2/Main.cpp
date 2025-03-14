#include "Point.hpp"
#include "Kmeans.hpp"
#include <stdlib.h>

int main() {
  srand(time(NULL));

  Kmeans *KM = new Kmeans(50,4);
  (*KM).initialiser();
  (*KM).calculer(5);

  (*KM).csv();

  return 0;
}
