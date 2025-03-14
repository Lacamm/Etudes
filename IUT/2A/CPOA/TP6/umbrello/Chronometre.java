
public class Chronometre implements IEvenement {

  private Automate contexte;  public Chronometre () { };
  
  //
  // Methods
  //


  /**
   * Set the value of contexte
   * @param newVar the new value of contexte
   */
  private void setContexte (Automate newVar) {
    contexte = newVar;
  }

  /**
   * Get the value of contexte
   * @return the value of contexte
   */
  private Automate getContexte () {
    return contexte;
  }

  //
  // Other methods
  //

  /**
   */
  public void lancerChrono()
  {
    contexte.lancerChrono();
  }


  /**
   */
  public void arreterChrono()
  {
    contexte.arreterChrono()
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
