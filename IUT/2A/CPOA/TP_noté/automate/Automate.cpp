#include "Automate.h"

// Constructors/Destructors
//  

Automate::Automate () {
initAttributes();
}

Automate::~Automate () { }

//  
// Methods
//  


// Accessor methods
//  


/**
 * Set the value of m_etatcourant
 * @param new_var the new value of m_etatcourant
 */
void Automate::setEtatCourant (IEtat * new_var) {
  m_etatcourant = new_var;
}

/**
 * Get the value of m_etatcourant
 * @return the value of m_etatcourant
 */
IEtat * Automate::getEtatCourant () {
  return m_etatcourant;
}

// Other methods
//  

void Automate::initAttributes () {
  m_etatcourant = new IEtat();
}

