
import java.util.*;

public class Prairie {

  //
  // Fields
  //

  private int carotte;
  private int posX;
  private int PosY;  
  public Prairie () {}
  public Prairie (int posX, int PosY, int nbCarotte) {
    this.posX = posX;
    this.posy = posY;
    this.carotte = nbCarotte;
  }
  //
  // Methods
  //


  //
  // Accessor methods
  //

  /**
   * Set the value of carotte
   * @param newVar the new value of carotte
   */
  private void setCarotte (int newVar) {
    carotte = newVar;
  }

  /**
   * Get the value of carotte
   * @return the value of carotte
   */
  private int getCarotte () {
    return carotte;
  }

  /**
   * Set the value of posX
   * @param newVar the new value of posX
   */
  private void setPosX (int newVar) {
    posX = newVar;
  }

  /**
   * Get the value of posX
   * @return the value of posX
   */
  private int getPosX () {
    return posX;
  }

  /**
   * Set the value of PosY
   * @param newVar the new value of PosY
   */
  private void setPosY (int newVar) {
    PosY = newVar;
  }

  /**
   * Get the value of PosY
   * @return the value of PosY
   */
  private int getPosY () {
    return PosY;
  }

  //
  // Other methods
  //

  /**
   */
  public void ajouterCarotte()
  {
    this.Carotte+=1;
  }

  public void supprimerCarotte()
  {
    this.Carotte-=1;
  }
  public String toString(){
    return "|| nb_Car : " + this.carotte + " - Ani : ||"
  }

}
