
typedef struct {
  char name[3];
  int adr;
} symbole;// élément de base pour la table des symboles

union value {
  int n;
  char name[3];
};

typedef struct {
  char type; //0 si entier, 1 si numéro de registre, 2 si adr absolue, 3 si adr relative par référence, 4 si adresse relative entière
  union value val;  //soit un entier, soit une référence
} targ;

typedef struct {
  char *def;
  char *name;
  char nbarg; //nombre d'arguments (1 ou 2)
  targ *args;
} casemem;

typedef struct {
  int nbinstr; // en nombre d'instructions
  casemem *listeinstr;
  int memsize;
  casemem *mem;
} module;


void affichecode(int nbinstr, casemem *linstr);
// affichage dans le terminal d'une liste d'instruction, la premiere colonne donne la representation memoire utilisee ici, la seconde est de type langage d'assemblage

void affichedon(int nbinstr, int memsize, casemem *mem);
// affichage dans le terminal d'une zone mémoire avec références éventuelles

void afficheram(int deb, int ramsize, casemem *ram);
// affichage dans le terminal d'une partie de la ram, la ligne de début est en rouge

targ newarg (char type, union value val);
//creation d'un element de type argument d'une instruction

casemem newcasemem (char * def,char *name,char nbarg, char type0, union value val0, char type1, union value val1);
//creation d'un element de type instruction

module newmod (int size,casemem *listeinstr,int memsize,casemem* mem);
  //creation d'un element de type module

int loader(int debut, module mod, casemem *mem);
// loader prend comme arguments la position de chargement en ram, le tableau des modules à charger et la liste des emplacements memoires, il retourne la premiere position qui suit les modules charges

module linker(int nbmods, module *mods);
//linker rassemble les modules en mettant les adresses en coherence : les adresses du second module sont decalees de la taille du premier, etc...
//linker remplit la table des symboles avec :
//-les refs de tous les modules : nom sans adresse
//-les defs de tous les modules : nom et adresse
//puis fait la resolution en parcourant tous les arguments de toutes les instructions pour remplacer les refs par les adresses obtenues dans la table des symboles
//le module construit est retourné par la fonction

module lect(char *fichier);
//lecture de la description d'un module dans le fichier et création du module

int recadr(symbole *table, int curr, char *name);
//recherche dans la table remplie jusqu'à (curr-1) de l'adresse de la référence name
