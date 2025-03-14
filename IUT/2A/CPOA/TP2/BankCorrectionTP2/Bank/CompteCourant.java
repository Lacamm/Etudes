import java.util.*;


public class CompteCourant extends Compte {

    private float decouvertAutorise = -100;
    private boolean bloque = false;
    private float plafondDebitClient = 1000;
    public static float plafondDebitDecouvertBank = 100;
    public static float plafondDebitMensuel = 3000;

    //=======================================
    public CompteCourant () { };
    public CompteCourant (String numero,float solde) {
        super(numero,solde);
    };

    //=======================================
    public void setDecouvertAutorise (float newVar) {
        decouvertAutorise = newVar;
    }

    //VERSION 0=======================================
    /*public boolean debiter(float montant, String info){
        if(montant>0){
            float res=this.solde-montant;
            if(res>=this.decouvertAutorise){
                this.solde=res;
                historique.addFirst(new Operation(info,-montant));
                return true;
            }
        }
        return false;
    }*/
    //VERSION 1=======================================
    /*public boolean debiter(float montant, String info){
        if(montant>0&&!bloque){
         float res=this.solde-montant;
         this.solde=res;
         historique.addFirst(new Operation(info,-montant));
         if(res<this.decouvertAutorise) this.bloque=true;
         return true;

        }
        System.out.println("Opération impossible - contactez votre banque");
        return false;
    }*/
    //VERSION 2+3+4=======================================
    public boolean debiter(float montant, String info){
        if(montant>0 && montant<=plafondDebitClient && !bloque && this.debitsMois()<plafondDebitMensuel){
            if(solde>0||montant<plafondDebitDecouvertBank){
                float res=this.solde-montant;
                this.solde=res;
                historique.addFirst(new Operation(info,-montant));
                if(res<decouvertAutorise) this.bloque=true;
                return true;
            }
        }
        System.out.println("Opération impossible - contactez votre banque");
        return false;
    }
    
    private float debitsMois(){
        boolean fenetre=true;
        float sommeDebits=0;
        ListIterator li = historique.listIterator();
        Date today=new Date();
        while(li.hasNext()&&fenetre){
            Operation op=(Operation) li.next();
            float val=op.getMontant();
            long diff=(op.getDate().getTime()-today.getTime())/(1000*60*60*24); //nb jours entre 2 dates
            if(diff<30){
                 if(val<0) sommeDebits=sommeDebits-val;
            }
            else fenetre=false;
        }
        System.out.println("Somme débits :"+sommeDebits);
        return sommeDebits;
    }
    
    public void debloquerCompte(){
        this.bloque=false;
    }

}
