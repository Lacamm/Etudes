#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "types.h"

void affinstr(casemem instr, int i) {
  printf("      %3d | ",i);
  printf("%6s ",instr.def);
  printf("%6s ",instr.name);
  for (int j=0;j<instr.nbarg;j++){
    if (instr.args[j].type == 3){
      printf(" (%d,%3s)",instr.args[j].type,instr.args[j].val.name);
    }
    else {
      printf(" (%d,%3d)",instr.args[j].type,instr.args[j].val.n);
    }
  }
  for (int j=instr.nbarg;j<2;j++){
    printf("        ");
  }
  printf("     |     ");
  printf("%3d | ",i);
  printf("%6s ",instr.def);
  printf("%6s ",instr.name);
  for (int j=0;j<instr.nbarg;j++){
    if (instr.args[j].type == 3){
      printf(" %3s",instr.args[j].val.name);
    }
    else {
      if (instr.args[j].type == 1){
	printf("  R%d",instr.args[j].val.n);
      }
      else {
	printf(" %3d",instr.args[j].val.n);
      }
    }
  }
  for (int j=instr.nbarg;j<2;j++){
    printf("    ");
  }
  printf("  |\n");
}

void affdon(casemem don, int i){
  printf("      %3d | ",i);
  printf("%6s",don.def);
  if (don.nbarg == 0){
    printf(" %3d",0);
  }
  else{
    printf(" %3d",don.args[0].val.n);
  }
  printf("  \n");
}

void affram(casemem casemem, int i) {
  printf("      %3d | ",i);
  if (strcmp(casemem.name,"mem")==0){
    printf("%6s ","");
    printf(" %5d        |\n",casemem.args[0].val.n);
  }
  else{
    if(strcmp(casemem.name,"empty")!=0){
      printf("%6s ",casemem.name);
    }
    else{
      printf("       ");
    }
    for (int j=0;j<casemem.nbarg;j++){
      if (casemem.args[j].type == 3){
	printf(" %5s",casemem.args[j].val.name);
      }
      else {
	if (casemem.args[j].type == 1){
	  printf("    R%d",casemem.args[j].val.n);
	}
	else {
	  printf("   %3d",casemem.args[j].val.n);
	}
      }
    }
    for (int j=casemem.nbarg;j<2;j++){
      printf("      ");
    }
    printf("  |\n");
  }
}

void affichecode(int nbinstr, casemem *linstr){ // affichage dans le terminal d'une liste d'instruction, la premiere colonne donne la representation memoire utilisee ici, la seconde est de type langage d'assemblage
  
  printf("      ****************************************************************************\n\n");
  printf("           ################Segment de code################\n");
  printf("       ____________________________________________________________________________\n");
  for (int i=nbinstr-1;i>=0;i--){
    affinstr(linstr[i],i);
  }
  printf("       ----------------------------------------------------------------------------\n");
}

void affichedon(int nbinstr,int memsize, casemem *mem){ // affichage dans le terminal d'une zone mémoire avec références éventuelles 
  printf("\n           ################Segment de données################\n");
  printf("       ____________________________________________________________________________\n");
  for (int i=memsize-1;i>=0;i--){
    affdon(mem[i],nbinstr+i);
  }
  printf("       ----------------------------------------------------------------------------\n");
}

void afficheram(int deb, int ramsize, casemem *mem){// affichage dans le terminal d'une partie de la ram
  printf("\n           ################Mémoire centrale################\n");
  printf("       __________________________\n");
  for (int i=ramsize-1;i>=0;i--){
    if (deb==i){
      printf("\033[0;31m"); 
    }
    affram(mem[i],i);
    if (deb==i){
      printf("\033[0m"); 
    }
  }
  printf("       --------------------------\n");
}



targ newarg (char type, union value val){ //creation d'un element de type argument d'une instruction
  targ arg = {type, val};
  return arg;
}

casemem emptycasemem(){
  casemem c;
  c.def="_";
  c.name="mem";
  c.nbarg=0;
  return c;
}

casemem newcasemem (char *def,char *name,char nbarg, char type0, union value val0, char type1, union value val1){ //creation d'un element de type instruction
  casemem c = emptycasemem();
  c.def=strdup(def);
  c.name=strdup(name);
  c.nbarg = nbarg;
  c.args = (targ *)malloc(c.nbarg * sizeof(targ));
  c.args[0]=newarg(type0, val0);
  if (nbarg==2){
    c.args[1]=newarg(type1, val1);
  };
  return(c);
}

module newmod (int nbinstr,casemem *listeinstr,int memsize,casemem *mem){
  //creation d'un element de type module
  module mod;
  mod.nbinstr = nbinstr;
  mod.listeinstr = listeinstr;
  mod.memsize = memsize;
  mod.mem = mem;
  return mod;
}


casemem instroflg(char* def, char* comm,char* arg1,char* arg2){
  union value empty;
  union value a1;
  union value a2 ;
  if (strcmp(comm, "pushr")==0){
    a1.n = atoi(arg1);
    return newcasemem(def,comm,1,1,a1,0,empty);
  }
  if (strcmp(comm, "pushv")==0){
    a1.n = atoi(arg1);
    return newcasemem(def,comm,1,0,a1,0,empty);
  }
  if (strcmp(comm, "pusha")==0){
    strcpy(a1.name,arg1);
    return newcasemem(def,comm,1,3,a1,0,empty);
  }
  if (strcmp(comm, "pop")==0){
    a1.n = atoi(arg1);
    return newcasemem(def,comm,1,1,a1,0,empty);
  }
  if (strcmp(comm, "call")==0){
    strcpy(a1.name,arg1);
    return newcasemem(def,comm,1,3,a1,0,empty);
  }
  if (strcmp(comm, "add")==0){
    a2.n = atoi(arg2);
    a1.n = atoi(arg1);
    return newcasemem(def,comm,2,1,a1,1,a2);
  }
  if (strcmp(comm, "jeq")==0){
    strcpy(a1.name,arg1);
    return newcasemem(def,comm,1,3,a1,0,empty);
  }
  if (strcmp(comm, "jse")==0){
    strcpy(a1.name,arg1);
    return newcasemem(def,comm,1,3,a1,0,empty);
  }
  if (strcmp(comm, "jmp")==0){
    strcpy(a1.name,arg1);
    return newcasemem(def,comm,1,3,a1,0,empty);
  }    
  if (strcmp(comm, "print")==0){
    a1.n = atoi(arg1);
    return newcasemem(def,comm,1,1,a1,0,empty);
  }
  if (strcmp(comm, "rdmem")==0){
    a2.n = atoi(arg2);
    a1.n = atoi(arg1);
    return newcasemem(def,comm,2,1,a1,1,a2);
  }
  if (strcmp(comm, "cmp")==0){
    a2.n = atoi(arg2);
    a1.n = atoi(arg1);
    return newcasemem(def,comm,2,1,a1,0,a2);
  }
  if (strcmp(comm, "inc")==0){
    a1.n = atoi(arg1);
    return newcasemem(def,comm,1,1,a1,0,empty);
  }
  if (strcmp(comm, "dec")==0){
    a1.n = atoi(arg1);
    return newcasemem(def,comm,1,1,a1,0,empty);
  }
  if (strcmp(comm, "ret")==0){
    a1.n = atoi(arg1);
    return newcasemem(def,comm,1,1,a1,0,empty);
  }  
}

casemem memoflg(char* def, char* arg1){
  union value empty;
  union value a1;
  a1.n = atoi(arg1);
  return newcasemem(def,"mem",1,0,a1,0,empty);
}

module lect(char* fichier)
{//lecture dans un fichier donné en paramètre des segments de code et de données, puis construction du module associé
   FILE * pFile;
   int nbinstr = 0;
   int memsize = 0;
   char *args[4];
   args[2]="";
   int nbarg = 0;
   int num = 0;
   char *lg;
   char sep[] = ", \t\n";
   size_t len = 0;
   ssize_t read;
   pFile = fopen (fichier, "r");
   read = getline(&lg, &len, pFile);
   char *mot = strtok(lg, sep);
   if (mot != NULL){
     nbinstr = atoi(mot);
   }
   casemem *listeinstr = (casemem *)malloc(nbinstr * sizeof(casemem));
   int i = 0;
   while (i < nbinstr) {
     read = getline(&lg, &len, pFile);
     mot = strtok(lg, sep);
     nbarg = 0;
     while(mot != NULL)
       {
	 args[nbarg]=mot;
	 nbarg = nbarg + 1;
	 mot = strtok(NULL, sep);
       }
     listeinstr[i]=instroflg(args[0],args[1],args[2],args[3]);
     i = i + 1;
   }
   read = getline(&lg, &len, pFile);
   mot = strtok(lg, sep);
   if (mot != NULL){
     memsize = atoi(mot);
   }
   casemem *mem = (casemem *)malloc(memsize*sizeof(casemem));
   i = 0;
   read = getline(&lg, &len, pFile);
   while (strlen(lg) != 1) {
     mot = strtok(lg, sep);
     num = 0;
     while(mot != NULL) {
       args[num]=mot;
       num = num + 1;
       mot = strtok(NULL, sep);
     }
     mem[i]=memoflg(args[0],args[1]);
     i = i + 1;
     read = getline(&lg, &len, pFile);
   }
   for (i;i<memsize;i++){
     mem[i]=emptycasemem();
   }
   
   fclose (pFile);
   module x=newmod(nbinstr,listeinstr,memsize,mem);
   return x;
 }

int recadr(symbole *table, int curr, char *name){//recherche dans la table remplie jusqu'à (curr-1) de l'adresse de la référence name
  int i = 0;
  while (i<curr){
    if (strcmp(table[i].name,name) == 0){
      return table[i].adr;
    }
    i=i+1;
  }
  printf("référence inconnue : %s",name);
  return -1;
}
