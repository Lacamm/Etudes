
import java.util.*;

public class Monde {

  //
  // Fields
  //


  private Vector prairiesVector = new Vector();

  private Monde m_leMonde;
  public Monde () { };
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

  /**
   * Add a Prairies object to the prairiesVector List
   */
  private void addPrairies (Prairie new_object) {
    prairiesVector.add(new_object);
  }

  /**
   * Remove a Prairies object from prairiesVector List
   */
  private void removePrairies (Prairie new_object)
  {
    prairiesVector.remove(new_object);
  }

  /**
   * Get the List of Prairies objects held by prairiesVector
   * @return List of Prairies objects held by prairiesVector
   */
  private List getPrairiesList () {
    return (List) prairiesVector;
  }


  /**
   * Set the value of m_leMonde
   * @param newVar the new value of m_leMonde
   */
  private void setLeMonde (Monde newVar) {
    m_leMonde = newVar;
  }

  /**
   * Get the value of m_leMonde
   * @return the value of m_leMonde
   */
  private Monde getLeMonde () {
    return m_leMonde;
  }

  //
  // Other methods
  //



}
