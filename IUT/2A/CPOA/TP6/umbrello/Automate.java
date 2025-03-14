
import java.util.*;

public class Automate implements IEvenement {

  //
  // Fields
  //

  private Chronometre controle;

  public IEtat m_etatCourant;  public Automate () { };
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

  /**
   * Set the value of controle
   * @param newVar the new value of controle
   */
  private void setControle (Chronometre newVar) {
    controle = newVar;
  }

  /**
   * Get the value of controle
   * @return the value of controle
   */
  private Chronometre getControle () {
    return controle;
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
   * @param        etat
   */
  public void changementEtat(IEtat etat)
  {
  }


  /**
   */
  public void evenement1()
  {
  }


  /**
   */
  public void evenement2()
  {
  }


}
