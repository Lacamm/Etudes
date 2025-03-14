
import java.util.*;

public class AutomateAnimal implements IEvenement {

  //
  // Fields
  //


  private Animal m_controle;

  private IEtat m_etatCourant;  public AutomateAnimal () { };
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

  /**
   * Set the value of m_controle
   * @param newVar the new value of m_controle
   */
  private void setControle (Animal newVar) {
    m_controle = newVar;
  }

  /**
   * Get the value of m_controle
   * @return the value of m_controle
   */
  private Animal getControle () {
    return m_controle;
  }

  /**
   * Set the value of m_etatCourant
   * @param newVar the new value of m_etatCourant
   */
  private void setEtatCourant (IEtat newVar) {
    m_etatCourant = newVar;
  }

  /**
   * Get the value of m_etatCourant
   * @return the value of m_etatCourant
   */
  private IEtat getEtatCourant () {
    return m_etatCourant;
  }

  //
  // Other methods
  //

  /**
   * @param        etat
   */
  public void changementEtat(IEtat etat)
  {
  }


  /**
   */
  public void seNourrir()
  {
  }


  /**
   */
  public void seReproduire()
  {
  }


  /**
   */
  public void seDeplacer()
  {
  }


}
