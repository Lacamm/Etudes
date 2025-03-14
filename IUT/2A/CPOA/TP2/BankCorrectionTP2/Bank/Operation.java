
import java.util.*;

public class Operation {

    private Date dateOp;
    private String libelle;
    private float montant;
    
    public Operation (String info,float montant){
        this.dateOp=new Date();
        this.libelle=info;
        this.montant=montant;
    };
    
    public float getMontant () {
        return montant;
    }

    public Date getDate () {
        return dateOp;
    }
    
    public String toString(){
        return this.dateOp+" "+this.libelle+" "+this.montant;
    }
}
