
import java.util.*;

public class AutomateAnimal implements IEvenement {

  //
  // Fields
  //


  public Animal m_contexte;

  public IEtat m_etatCourant;  public AutomateAnimal () { };
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

  /**
   * Set the value of m_contexte
   * @param newVar the new value of m_contexte
   */
  public void setContexte (Animal newVar) {
    m_contexte = newVar;
  }

  /**
   * Get the value of m_contexte
   * @return the value of m_contexte
   */
  public Animal getContexte () {
    return m_contexte;
  }

  /**
   * Set the value of m_etatCourant
   * @param newVar the new value of m_etatCourant
   */
  public void setEtatCourant (IEtat newVar) {
    m_etatCourant = newVar;
  }

  /**
   * Get the value of m_etatCourant
   * @return the value of m_etatCourant
   */
  public IEtat getEtatCourant () {
    return m_etatCourant;
  }

  //
  // Other methods
  //

  /**
   * @return       Etat
   * @param        etat
   */
  public Etat changerEtat(Etat etat)
  {
    return null;
  }


  /**
   */
  public void seReproduire()
  {
  }


  /**
   */
  public void seNourrir()
  {
  }


}
