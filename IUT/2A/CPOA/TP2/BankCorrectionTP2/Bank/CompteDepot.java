
public class CompteDepot extends Compte {

    public static float soldeMinimum = 0;
    public static float tauxInteret;
    //=======================================
    public CompteDepot () { };
    public CompteDepot (String numero,float solde) {
        super(numero,solde);
    };
    //=======================================
    public boolean debiter(float montant, String info){
        if(montant>0){
            float res=this.solde-montant;
            if(res>=this.soldeMinimum){
                this.solde=res;
                historique.addFirst(new Operation(info,-montant));
                return true;
                }
            }
        return false;
    }
}
