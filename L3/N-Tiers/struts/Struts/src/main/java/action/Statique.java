package action;

import com.opensymphony.xwork2.ActionSupport;

import java.util.Arrays;
import java.util.Collection;

public class Statique extends ActionSupport {

    float operande1, operande2, resultat;
    Collection<String> operateur;
    String symbole;

    public float getOperande1() {
        return operande1;
    }
    public float getOperande2() {
        return operande2;
    }
    public float getResultat(){
        return resultat;
    }
    public String getSymbole() {return symbole;}

    public Collection<String> getOperateur() {;
        return Arrays.asList(
                "Addition",
                "Soustraction",
                "Multiplication",
                "Division"
        );
    }

    public void setOperande1(float nombre1) {
        this.operande1 = nombre1;
    }
    public void setOperande2(float nombre2) {
        this.operande2 = nombre2;
    }
    public void setSymbole(String str){
        this.symbole = str;
    }


    public float operation(float n1, float n2, String operateur){
        switch(operateur){
            case "Addition":
                this.resultat = n1+n2;
                break;
            case "Soustraction":
                this.resultat = n1-n2;
                break;
            case "Multiplication":
                this.resultat = n1*n2;
                break;
            case "Division":
                this.resultat = n1/n2;
                break;
        }
        return resultat;
    }

    public String execute(){
        operation(operande1,operande2,symbole);
        return SUCCESS;
    }
}
