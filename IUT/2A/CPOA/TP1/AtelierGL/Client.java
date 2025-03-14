
import java.util.*;

public class Client {

  //
  // Fields
  //

  private String nom;
  private Vector<Compte> comptesVector;

  private Vector comptesVector = new Vector();  public Client () { };
  
  //
  // Methods
  //


  //
  // Accessor methods
  //

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
   * Set the value of comptesVector
   * @param newVar the new value of comptesVector
   */
  private void setComptesVector (Vector<Compte> newVar) {
    comptesVector = newVar;
  }

  /**
   * Get the value of comptesVector
   * @return the value of comptesVector
   */
  private Vector<Compte> getComptesVector () {
    return comptesVector;
  }

  /**
   * Add a Comptes object to the comptesVector List
   */
  private void addComptes (Compte new_object) {
    comptesVector.add(new_object);
  }

  /**
   * Remove a Comptes object from comptesVector List
   */
  private void removeComptes (Compte new_object)
  {
    comptesVector.remove(new_object);
  }

  /**
   * Get the List of Comptes objects held by comptesVector
   * @return List of Comptes objects held by comptesVector
   */
  private List getComptesList () {
    return (List) comptesVector;
  }


  //
  // Other methods
  //

  /**
   */
  public void Client()
  {
  }


  /**
   * @param        nom
   */
  public void Client(String nom)
  {
  }


  /**
   * @param        newVar
   */
  public void setNom(String newVar)
  {
  }


  /**
   * @return       String
   */
  public String getNom()
  {
  }


  /**
   * @param        new_object
   */
  public void addComptes(Compte new_object)
  {
  }


  /**
   * @param        new_object
   */
  public void removeComptes(Compte new_object)
  {
  }


  /**
   * @return       List
   */
  public List getComptesList()
  {
  }


  /**
   * @return       Compte
   * @param        numero
   */
  public Compte getCompte(String numero)
  {
  }


}
