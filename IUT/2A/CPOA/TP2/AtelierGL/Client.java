
import java.util.*;

public class Client {


  private String nom;

  private Vector<Compte> comptesVector = new Vector();
    
    public Client () { };
    
    public Client (String nom) {
        this.nom=nom;
    };

  public void setNom (String newVar) {
    nom = newVar;
  }

  public String getNom () {
    return nom;
  }

  public void addComptes (Compte new_object) {
    comptesVector.add(new_object);
  }

  public void removeComptes (Compte new_object)
  {
    comptesVector.remove(new_object);
  }

  public List getComptesList () {
    return (List) comptesVector;
  }

    
    public Compte getCompte(String numero){
        List l=this.getComptesList();
        for(int i = 0; i < l.size(); i++){
            Compte co=(Compte)l.get(i);
            if(numero.equals(co.getNumero())) return co;
        }
        return null;
    }

}
