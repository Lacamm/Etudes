#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "types.h"


int loader(int debut, module mod, casemem *mem) {

  int indexdeb = 0;
  int indexinstr = 0;

  for(int i=0;i<mod.nbinstr;i++){
    indexinstr = debut+1+i;
    mem[indexinstr] = mod.listeinstr[i];
    if(strcmp(mod.listeinstr[i].def, "deb")==0){indexdeb = indexinstr;}
    if(mod.listeinstr[i].args[0].type == 4){mod.listeinstr[i].args[0].val.n += debut+1;}  
  }

  for(int i=0;i<mod.memsize;i++){
    indexinstr = debut+1+i+mod.nbinstr;
    mem[indexinstr] = mod.mem[i];
  }

  mem[debut].name = "call";
  mem[debut].args = (targ*) malloc(sizeof(targ));
  mem[debut].args->val.n = indexdeb; 

  return debut;
}
