
#ifndef PRAIRIES_H
#define PRAIRIES_H
#include "undef.h"
#include "Biome.h"

#include chaîne
class Prairies : public undef, public Biome
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  Prairies ();

  /**
   * Empty Destructor
   */
  virtual ~Prairies ();



  /**
   */
  void croissanceCarotte ()
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

  int nbCarotte;
public:

private:

public:


  // Private attribute accessor methods
  //  


  /**
   * Set the value of nbCarotte
   * @param new_var the new value of nbCarotte
   */
  void setNbCarotte (int new_var)   {
      nbCarotte = new_var;
  }

  /**
   * Get the value of nbCarotte
   * @return the value of nbCarotte
   */
  int getNbCarotte ()   {
    return nbCarotte;
  }
private:


  void initAttributes () ;

};

#endif // PRAIRIES_H
