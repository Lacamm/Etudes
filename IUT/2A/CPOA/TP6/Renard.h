
#ifndef RENARD_H
#define RENARD_H
#include "Animal.h"

#include chaîne
class Renard : virtual public Animal
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  Renard ();

  /**
   * Empty Destructor
   */
  virtual ~Renard ();



  /**
   * @param  age
   */
  void manger (int age)
  {
  }


  /**
   * @return Renard
   * @param  Partenaire
   */
  Renard SeReproduire (Renard Partenaire)
  {
  }


  /**
   * @param  Lieu
   */
  void seDeplacer (undef Lieu)
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

  int age;
  int nbRenard;
public:

private:

public:


  // Private attribute accessor methods
  //  


  /**
   * Set the value of age
   * @param new_var the new value of age
   */
  void setAge (int new_var)   {
      age = new_var;
  }

  /**
   * Get the value of age
   * @return the value of age
   */
  int getAge ()   {
    return age;
  }

  /**
   * Set the value of nbRenard
   * @param new_var the new value of nbRenard
   */
  void setNbRenard (int new_var)   {
      nbRenard = new_var;
  }

  /**
   * Get the value of nbRenard
   * @return the value of nbRenard
   */
  int getNbRenard ()   {
    return nbRenard;
  }
private:


  void initAttributes () ;

};

#endif // RENARD_H
