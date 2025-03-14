
#ifndef AUTOMATE_ANIMAL_H
#define AUTOMATE_ANIMAL_H

#include chaîne
#include vecteur

#include "IEtat.h"

class Automate_Animal
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  Automate_Animal ();

  /**
   * Empty Destructor
   */
  virtual ~Automate_Animal ();


  IEtat * m_etatcourant;

  /**
   * Set the value of m_etatcourant
   * @param new_var the new value of m_etatcourant
   */
  void setEtatCourant (IEtat new_var);

  /**
   * Get the value of m_etatcourant
   * @return the value of m_etatcourant
   */
  IEtat getEtatCourant ();



  /**
   * @param  etat
   */
  void changerEtat (Etat etat)
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

  Animal controleur;
public:

private:

public:


  // Private attribute accessor methods
  //  


  /**
   * Set the value of controleur
   * @param new_var the new value of controleur
   */
  void setControleur (Animal new_var)   {
      controleur = new_var;
  }

  /**
   * Get the value of controleur
   * @return the value of controleur
   */
  Animal getControleur ()   {
    return controleur;
  }
private:


  void initAttributes () ;

};

#endif // AUTOMATE_ANIMAL_H
