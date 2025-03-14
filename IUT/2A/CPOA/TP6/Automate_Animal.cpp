#include "Automate_Animal.h"

// Constructors/Destructors
//  

Automate_Animal::Automate_Animal () {
initAttributes();
}

Automate_Animal::~Automate_Animal () { }

//  
// Methods
//  


// Accessor methods
//  


/**
 * Set the value of m_etatcourant
 * @param new_var the new value of m_etatcourant
 */
void Automate_Animal::setEtatCourant (IEtat * new_var) {
  m_etatcourant = new_var;
}

/**
 * Get the value of m_etatcourant
 * @return the value of m_etatcourant
 */
IEtat * Automate_Animal::getEtatCourant () {
  return m_etatcourant;
}

// Other methods
//  

void Automate_Animal::initAttributes () {
  m_etatcourant = new IEtat();
}

