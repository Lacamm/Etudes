
import java.util.*;

public class Compte {

    private float solde;
    private String numero;
    private float decouvertAutorise = 0;
    
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

    public void setDecouvertAutorise (float newVar) {
        decouvertAutorise = newVar;
    }

    public float getDecouvertAutorise () {
        return decouvertAutorise;
    }
    //=======================================
    public boolean debiter(float montant,String info){
        if(montant>0){
            float res=this.solde-montant;
            if(res>=this.decouvertAutorise){
                this.solde=res;
                historique.addFirst(new Operation(info,-montant));
                return true;
            }
        }
        return false;
    }

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
