
import java.util.*;

public abstract class Compte {

    protected float solde;
    protected String numero;
    
    LinkedList<Operation> historique = new LinkedList();
    
    //=======================================
    public Compte () { };
    
    public Compte (String numero,float solde) {
        this.numero=numero;
        this.solde=solde;
    };
    //=======================================
    public void setSolde (float newVar) {
        solde = newVar;
    }

    public float getSolde () {
        return solde;
    }

    public void setNumero (String newVar) {
        numero = newVar;
    }

    public String getNumero () {
        return numero;
    }
    //=======================================
    public abstract boolean debiter(float montant,String info);

    public boolean crediter(float montant,String info){
        if(montant>0){
            this.solde+=montant;
            historique.addFirst(new Operation(info,montant));
            return true;
        }
        else return false;
    }

    public void afficherHistorique(){
        System.out.println("=====HISTORIQUE=====");
        ListIterator li = historique.listIterator();
        while(li.hasNext())
            System.out.println(li.next());
    }
    
    public String toString(){
        return "Compte numéro : "+this.numero+" - Solde :"+this.solde;
    }


}
