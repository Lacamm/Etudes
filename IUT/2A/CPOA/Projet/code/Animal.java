
import java.util.*;

public class Animal implements IEvenement {

  //
  // Fields
  //

  private String sexe;
  private int energie;
  private int age;

  public AutomateAnimal m_controleur;
  
  public Animal (String sexe, int energie, int age) { 
    this.sexe = sexe;
    this.energie = energie;
    this.age = age;
  };
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

  /**
   * Set the value of sexe
   * @param newVar the new value of sexe
   */
  public void setSexe (String newVar) {
    sexe = newVar;
  }

  /**
   * Get the value of sexe
   * @return the value of sexe
   */
  public String getSexe () {
    return sexe;
  }

  /**
   * Set the value of energie
   * @param newVar the new value of energie
   */
  public void setEnergie (int newVar) {
    energie = newVar;
  }

  /**
   * Get the value of energie
   * @return the value of energie
   */
  public int getEnergie () {
    return energie;
  }

  /**
   * Set the value of age
   * @param newVar the new value of age
   */
  public void setAge (int newVar) {
    age = newVar;
  }

  /**
   * Get the value of age
   * @return the value of age
   */
  public int getAge () {
    return age;
  }

  /**
   * Set the value of m_controleur
   * @param newVar the new value of m_controleur
   */
  public void setControleur (AutomateAnimal newVar) {
    m_controleur = newVar;
  }

  /**
   * Get the value of m_controleur
   * @return the value of m_controleur
   */
  public AutomateAnimal getControleur () {
    return m_controleur;
  }

  //
  // Other methods
  //

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


  /**
   */
  public void seDeplacer()
  {
  }


}
