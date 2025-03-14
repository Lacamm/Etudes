#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "types.h"


int main(int argc, char **argv) {
  
  int ramsize = 50;
  casemem *ram = (casemem *)malloc(ramsize * sizeof(casemem));
  int pos = 4;
  casemem vide = {"","empty",0,NULL};
  
  for (int i=0;i<ramsize;i++){
    ram[i] = vide;
  }

  //lecture des 2 modules depuis les fichiers de description
  module m0 = lect("module0.dat");
  module m1 = lect("module1.dat");
  module modules[2] = {m0,m1};
  
  printf("Modules avant édition de liens :\n");
  affichecode(modules[0].nbinstr,modules[0].listeinstr);
  affichedon(modules[0].nbinstr,modules[0].memsize,modules[0].mem);
  affichecode(modules[1].nbinstr,modules[1].listeinstr);
  affichedon(modules[1].nbinstr,modules[1].memsize,modules[1].mem);
  
  //édition de liens, les 2 modules deviennent un seul
  module modlinked = linker(2,modules);
  printf("Module après édition de liens :\n");
  affichecode(modlinked.nbinstr,modlinked.listeinstr);
  affichedon(modlinked.nbinstr,modlinked.memsize,modlinked.mem);

  //chargement
  int suite = loader(pos,modlinked,ram);
  printf("Mémoire après chargement :\n");
  afficheram(pos,ramsize,ram);

  free(ram);

  return 0;
}



  
  
