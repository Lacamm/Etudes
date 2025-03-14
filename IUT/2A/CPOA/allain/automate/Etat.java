
import java.util.*;

public class Etat {

  //
  // Fields
  //
  private String mot;
  private Boolean res;
  public Etat () { };
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

  //
  // Other methods
  //

  /**
   * @return       String
   */
  public String get_InitialState()
  {
    this.mot =  InitialState.get_Mot();
  }


  /**
   * @return       String
   * @param        mot
   */
  public String get_Transition(String mot)
  {
    this.mot = Transition.treate_a_word(this.mot);
    this.res = Transition.get_res();    
  }


  /**
   * @return       Boolean
   * @param        mot
   */
  public Boolean get_FinalState(String mot)
  {
    FinalState.valider_mot(this.res);
  }


}
