
#ifndef AUTOMATE_H
#define AUTOMATE_H
#include "IEvenement.h"

#include chaîne
#include vecteur

#include "IEtat.h"

class Automate : virtual public IEvenement
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  Automate ();

  /**
   * Empty Destructor
   */
  virtual ~Automate ();


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
  void changementEtat (IEtat etat)
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

  X controle;
public:

private:

public:


  // Private attribute accessor methods
  //  


  /**
   * Set the value of controle
   * @param new_var the new value of controle
   */
  void setControle (X new_var)   {
      controle = new_var;
  }

  /**
   * Get the value of controle
   * @return the value of controle
   */
  X getControle ()   {
    return controle;
  }
private:


  void initAttributes () ;

};

#endif // AUTOMATE_H
