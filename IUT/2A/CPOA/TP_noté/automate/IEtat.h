
#ifndef IETAT_H
#define IETAT_H

#include chaîne
#include vecteur


/******************************* Abstract Class ****************************
IEtat does not have any pure virtual methods, but its author
  defined it as an abstract class, so you should not use it directly.
  Inherit from it instead and create only objects from the derived classes
*****************************************************************************/

class IEtat
{
public:



  /**
   * @param  a
   */
  virtual void evenement1 (Automate a)
  {
  }


  /**
   * @param  a
   */
  virtual void evenement2 (Automate a)
  {
  }

protected:

public:

protected:

public:

protected:


private:

public:

private:

public:

private:



};

#endif // IETAT_H
