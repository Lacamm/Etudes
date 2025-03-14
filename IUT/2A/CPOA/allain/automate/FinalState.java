
import java.util.*;

public class FinalState extends Etat {

  //
  // Fields
  //
  public FinalState () { };
  
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
   * @param        res
   */
  public String valider_mot(boolean res)
  {
    if (res){
      System.out.println("Le mot: "+MyAutomate.getMot()+" est reconnu par l'automate");
    }
    else{
      System.out.println("Le mot: "+MyAutomate.getMot()+" n'est pas reconnu par l'automate");
    }
  }
}
