package action;

import com.opensymphony.xwork2.ActionSupport;
import modele.CalculatriceDynamiqueDuFutur;
import modele.CalculatriceDynamiqueDuFuturImpl;

import java.util.Arrays;
import java.util.Collection;

public class Dynamique extends ActionSupport {

    double operande1, operande2, resultat;
    String symbole;
    CalculatriceDynamiqueDuFutur ope = new CalculatriceDynamiqueDuFuturImpl();

    public double getOperande1() {
        return operande1;
    }
    public double getOperande2() {
        return operande2;
    }
    public double getResultat(){
        return resultat;
    }
    public String getSymbole() {return symbole;}

    public void setOperande1(float nombre1) {
        this.operande1 = nombre1;
    }
    public void setOperande2(float nombre2) {
        this.operande2 = nombre2;
    }
    public void setSymbole(String str){
        this.symbole = str;
    }

    public Collection<String> getOperateur() {;
        return ope.getOperations();
    }

    public String execute(){

        try {
            resultat = ope.doCalcul(symbole,operande1,operande2);
        }
        catch(Exception e){
            System.out.println(e);
        };
        return SUCCESS;
    }
}
