
import java.util.*;

public class Transition extends Etat {

  //
  // Fields
  //


  public Vector resVector = new Vector();  public Transition () { };
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

  /**
   * Add a Res object to the resVector List
   */
  public void addRes (FinalState new_object) {
    resVector.add(new_object);
  }

  /**
   * Remove a Res object from resVector List
   */
  public void removeRes (FinalState new_object)
  {
    resVector.remove(new_object);
  }

  /**
   * Get the List of Res objects held by resVector
   * @return List of Res objects held by resVector
   */
  public List getResList () {
    return (List) resVector;
  }


  //
  // Other methods
  //

  /**
   * @return       String
   * @param        mot
   */
  public String treate_a_word(String mot)
  {


    
    return mot;
  }


  /**
   * @return       Boolean
   */
  public Boolean get_Res()
  {
    return MyAutomate.getRes();
  }


}
