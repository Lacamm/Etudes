
#ifndef ANIMAL_H
#define ANIMAL_H
#include "undef.h"

#include chaîne
#include vecteur


/******************************* Abstract Class ****************************
Animal does not have any pure virtual methods, but its author
  defined it as an abstract class, so you should not use it directly.
  Inherit from it instead and create only objects from the derived classes
*****************************************************************************/

class Animal : public undef
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  Animal ();

  /**
   * Empty Destructor
   */
  virtual ~Animal ();



  /**
   * @return Animal
   * @param  partenaire
   */
  Animal seReproduire (Animal partenaire)
  {
  }


  /**
   * @param  lieu
   */
  void seDeplacer (Biome lieu)
  {
  }


  /**
   * @param  aliment
   * @param  nbAliment
   */
  void manger (Nourriture aliment, int nbAliment)
  {
  }

protected:

public:

protected:

public:

protected:


private:

  // Private attributes
  //  

  String sexe;
  int energie;
  Automate_Animal contexte;
public:

private:

public:


  // Private attribute accessor methods
  //  


  /**
   * Set the value of sexe
   * @param new_var the new value of sexe
   */
  void setSexe (String new_var)   {
      sexe = new_var;
  }

  /**
   * Get the value of sexe
   * @return the value of sexe
   */
  String getSexe ()   {
    return sexe;
  }

  /**
   * Set the value of energie
   * @param new_var the new value of energie
   */
  void setEnergie (int new_var)   {
      energie = new_var;
  }

  /**
   * Get the value of energie
   * @return the value of energie
   */
  int getEnergie ()   {
    return energie;
  }

  /**
   * Set the value of contexte
   * @param new_var the new value of contexte
   */
  void setContexte (Automate_Animal new_var)   {
      contexte = new_var;
  }

  /**
   * Get the value of contexte
   * @return the value of contexte
   */
  Automate_Animal getContexte ()   {
    return contexte;
  }
private:


  void initAttributes () ;

};

#endif // ANIMAL_H
