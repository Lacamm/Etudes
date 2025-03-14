
#ifndef X_H
#define X_H
#include "IEvenement.h"

#include chaîne
class X : virtual public IEvenement
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  X ();

  /**
   * Empty Destructor
   */
  virtual ~X ();



  /**
   */
  void action1 ()
  {
  }


  /**
   */
  void action2 ()
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

  Automate contexte;
public:

private:

public:


  // Private attribute accessor methods
  //  


  /**
   * Set the value of contexte
   * @param new_var the new value of contexte
   */
  void setContexte (Automate new_var)   {
      contexte = new_var;
  }

  /**
   * Get the value of contexte
   * @return the value of contexte
   */
  Automate getContexte ()   {
    return contexte;
  }
private:


  void initAttributes () ;

};

#endif // X_H
