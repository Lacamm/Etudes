#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "types.h"

struct Reference{
  char* def;
  int index;
};


module linker(int nbmods, module *mods) {
  int nbinstr = 0; //code
  int memsize = 0; //données
  int nbsymb = 0;

  int cptdonnes = 0;
  
  //passe 1, créer un module unique pour les regrouper tous en décalant les adresses relatives dans chaque module
  //passe 2, remplir la table des symboles
  
  for (int i=0; i<nbmods;i++){
    nbinstr += mods[i].nbinstr;
    memsize += mods[i].memsize;
  }

  struct Reference* listRef = (struct Reference*)malloc(sizeof(struct Reference)*nbinstr);
  int nbref = 0;
  
  casemem *linstr = (casemem *)malloc(nbinstr * sizeof(casemem));
  casemem *mem = (casemem *)malloc(memsize * sizeof(casemem));
  

  for (int i=0; i<nbmods; i++){
    module* currentmodule = &mods[i];
    for (int j=0; j<currentmodule->nbinstr;j++){
      linstr[nbsymb] = currentmodule->listeinstr[j];
      if(strcmp(linstr[nbsymb].def, "_")!=0){
        listRef[nbref].def = linstr[nbsymb].def;
        listRef[nbref].index = nbsymb;
        nbref++;
      }
      nbsymb++;
    }
  }

  for (int i=0; i<nbmods; i++){
  module* currentmodule = &mods[i];
    for (int j=0; j<currentmodule->memsize;j++){
      mem[cptdonnes] = currentmodule->mem[j];
      if(strcmp(mem[cptdonnes].def, "_")!=0){
        listRef[nbref].def = mem[cptdonnes].def;
        listRef[nbref].index = nbsymb;
        nbref++;
      }
      nbsymb++;
      cptdonnes++;
    }
  }
 
  module mod = newmod(nbinstr,linstr,memsize,mem);

  //passe 3, remplacer pour chaque référence le nom par l'adresse de la définition

  for(int j=0; j<nbref;j++){
    printf("REF : %s %d\n", listRef[j].def, listRef[j].index);
  }


  for(int i=0; i<mod.nbinstr;i++){
    if(linstr[i].nbarg>=1 && linstr[i].args[0].type ==3 ){
      linstr[i].args[0].type = 4;
      for(int j=0; j<nbref;j++){
        if(strcmp(linstr[i].args[0].val.name, listRef[j].def)==0){
          linstr[i].args[0].val.n = listRef[j].index;
        }
      }
    }
  }
  
  return mod;
}
