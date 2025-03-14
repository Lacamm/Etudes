
#ifndef NOURRITURE_H
#define NOURRITURE_H

#include chaîne
/******************************* Abstract Class ****************************
Nourriture does not have any pure virtual methods, but its author
  defined it as an abstract class, so you should not use it directly.
  Inherit from it instead and create only objects from the derived classes
*****************************************************************************/

class Nourriture
{
public:

  // Constructors/Destructors
  //  


  /**
   * Empty Constructor
   */
  Nourriture ();

  /**
   * Empty Destructor
   */
  virtual ~Nourriture ();


protected:

public:

protected:

public:

protected:


private:

  // Private attributes
  //  

  String nom;
  String type;
public:

private:

public:


  // Private attribute accessor methods
  //  


  /**
   * Set the value of nom
   * @param new_var the new value of nom
   */
  void setNom (String new_var)   {
      nom = new_var;
  }

  /**
   * Get the value of nom
   * @return the value of nom
   */
  String getNom ()   {
    return nom;
  }

  /**
   * Set the value of type
   * @param new_var the new value of type
   */
  void setType (String new_var)   {
      type = new_var;
  }

  /**
   * Get the value of type
   * @return the value of type
   */
  String getType ()   {
    return type;
  }
private:


  void initAttributes () ;

};

#endif // NOURRITURE_H
