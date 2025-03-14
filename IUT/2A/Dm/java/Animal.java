
import java.util.*;

public class Animal implements IEvenement {

  //
  // Fields
  //

  private int energie;
  private boolean sexe;
  private int age;
  private int seuil;
  private int plafond;

  private AutomateAnimal m_contexte;
  public Animal () { };
  public Animal (int ener, boolean sexe, int age, int seuil, int plafond){
    this.energie=ener;
  }
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

  /**
   * Set the value of energie
   * @param newVar the new value of energie
   */
  private void setEnergie (int newVar) {
    energie = newVar;
  }

  /**
   * Get the value of energie
   * @return the value of energie
   */
  private int getEnergie () {
    return energie;
  }

  /**
   * Set the value of sexe
   * @param newVar the new value of sexe
   */
  private void setSexe (boolean newVar) {
    sexe = newVar;
  }

  /**
   * Get the value of sexe
   * @return the value of sexe
   */
  private boolean getSexe () {
    return sexe;
  }

  /**
   * Set the value of age
   * @param newVar the new value of age
   */
  private void setAge (int newVar) {
    age = newVar;
  }

  /**
   * Get the value of age
   * @return the value of age
   */
  private int getAge () {
    return age;
  }

  /**
   * Set the value of seuil
   * @param newVar the new value of seuil
   */
  private void setSeuil (int newVar) {
    seuil = newVar;
  }

  /**
   * Get the value of seuil
   * @return the value of seuil
   */
  private int getSeuil () {
    return seuil;
  }

  /**
   * Set the value of plafond
   * @param newVar the new value of plafond
   */
  private void setPlafond (int newVar) {
    plafond = newVar;
  }

  /**
   * Get the value of plafond
   * @return the value of plafond
   */
  private int getPlafond () {
    return plafond;
  }

  /**
   * Set the value of m_contexte
   * @param newVar the new value of m_contexte
   */
  private void setContexte (AutomateAnimal newVar) {
    m_contexte = newVar;
  }

  /**
   * Get the value of m_contexte
   * @return the value of m_contexte
   */
  private AutomateAnimal getContexte () {
    return m_contexte;
  }

  //
  // Other methods
  //

  /**
   */
  public void seDeplacer()
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


}
