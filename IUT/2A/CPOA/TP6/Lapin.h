
#ifndef LAPIN_H
#define LAPIN_H
#include "undef.h"
#include "Animal.h"

#include chaîne
class Lapin : public undef, virtual public Animal
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  Lapin ();

  /**
   * Empty Destructor
   */
  virtual ~Lapin ();



  /**
   * @return Lapin
   * @param  Partenaire
   */
  Lapin seReproduire (Lapin Partenaire)
  {
  }


  /**
   * @param  lieu
   */
  void seDeplacer (undef lieu)
  {
  }


  /**
   * @param  aliment
   * @param  nbCarotte
   */
  void manger (Carotte aliment, int nbCarotte)
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

  int nbLapin;
public:

private:

public:


  // Private attribute accessor methods
  //  


  /**
   * Set the value of nbLapin
   * @param new_var the new value of nbLapin
   */
  void setNbLapin (int new_var)   {
      nbLapin = new_var;
  }

  /**
   * Get the value of nbLapin
   * @return the value of nbLapin
   */
  int getNbLapin ()   {
    return nbLapin;
  }
private:


  void initAttributes () ;

};

#endif // LAPIN_H
