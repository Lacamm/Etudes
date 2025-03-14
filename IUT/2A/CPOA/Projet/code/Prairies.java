import java.util.*;

public class Prairies {

  private int posX;
  private int posY;
  private int nbCarotte;
  
  private List<Animal> lLapin;
  
  public Prairies (int nbCarotte, int posX, int posY) { 
    this.nbCarotte = nbCarotte;
    this.posX = posX;
    this.posY = posY;
    this.lLapin = new ArrayList<>();
  };
  
  //
  // Methods
  //

  /**
   * Set the value of posX
   * @param newVar the new value of posX
   */
  public void setPosX (int newVar) {
    posX = newVar;
  }

  /**
   * Get the value of posX
   * @return the value of posX
   */
  public int getPosX () {
    return posX;
  }

  /**
   * Set the value of posY
   * @param newVar the new value of posY
   */
  public void setPosY (int newVar) {
    posY = newVar;
  }

  /**
   * Get the value of posY
   * @return the value of posY
   */
  public int getPosY () {
    return posY;
  }

  /**
   * Set the value of nbCarotte
   * @param newVar the new value of nbCarotte
   */
  public void setNbCarotte (int newVar) {
    nbCarotte = newVar;
  }

  /**
   * Get the value of nbCarotte
   * @return the value of nbCarotte
   */
  public int getNbCarotte () {
    return nbCarotte;
  }

  //
  // Other methods
  //

  /**
   */
  public void croissanceCarotte(){
    this.nbCarotte ++;
  }

  public void addEspece(Animal a){
    if(a instanceof Lapin){
      this.lLapin.add(a);
    }
  }

  public List<Animal> getLapin(){
    return this.lLapin;
  }
  
  @Override

  public String toString(){
    String lieu = "Prairie en " + this.posX + "-" + this.posY + ", " + this.nbCarotte + " carottes\n";
    
    int f = 0;
    int m = 0;
    int a = -1;
    for(Animal l : this.lLapin){
      if (l.getSexe().equals("mâle")){m+=1;a = l.getAge();}
      else{f+=1;}
    }
    String lap = this.lLapin.size() + " lapins, " + m + " mâles," + f + " femelles\n";

    return lieu+lap;
  }
}
