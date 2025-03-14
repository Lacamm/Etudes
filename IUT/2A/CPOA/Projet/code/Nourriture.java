
public class Nourriture extends Biome {

  private String nom;
  private String type;
  
  public Nourriture (String nom, String type) { 
    this.nom = nom;
    this.type = type;
  };



  /**
   * Set the value of nom
   * @param newVar the new value of nom
   */
  private void setNom (String newVar) {
    nom = newVar;
  }

  /**
   * Get the value of nom
   * @return the value of nom
   */
  private String getNom () {
    return nom;
  }

  /**
   * Set the value of type
   * @param newVar the new value of type
   */
  private void setType (String newVar) {
    type = newVar;
  }

  /**
   * Get the value of type
   * @return the value of type
   */
  private String getType () {
    return type;
  }

}
