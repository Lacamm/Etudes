
import java.util.*;

public class MyAutomate {

  //
  // Fields
  //

  private String mot;
  private Boolean res;  public MyAutomate () { };
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

  /**
   * Set the value of mot
   * @param newVar the new value of mot
   */
  private void setMot (String newVar) {
    mot = newVar;
  }

  /**
   * Get the value of mot
   * @return the value of mot
   */
  private String getMot () {
    return mot;
  }

  /**
   * Set the value of res
   * @param newVar the new value of res
   */
  private void setRes (Boolean newVar) {
    res = newVar;
  }

  /**
   * Get the value of res
   * @return the value of res
   */
  private Boolean getRes () {
    return res;
  }
   
  public static void main(String [] args){
    String mot1 = "abb";
    String mot2 = "abab";

    Etat e0 = new Etat();
    Etat e1 = new Etat();

    e0.get_InitialState();
    
  } 
}
