import java.util.*;

public class Vente{
    private int idVe, prixBase, prixMin;
    private Objet objet;
    private String debutVe, finVe;
    private Statut statut;

    public Vente(int idVe, Objet objet, int prixBase, int prixMin, String debutVe, String finVe, Statut statut){
        this.idVe=idVe;
        this.objet=objet;
        this.prixBase=prixBase;
        this.prixMin=prixMin;
        this.debutVe=debutVe;
        this.finVe=finVe;
        this.statut=statut;
    }

    //GETTER 
    
    public int getIdVe(){
        return this.idVe;
    }

    public Objet getObjet(){
        return this.objet;
    }

    public int getPrixBase(){
        return this.prixBase;
    }

    public int getPrixMin(){
        return this.prixMin;
    }

    public String getDebutVe(){
        return this.debutVe;
    }

    public String getFinVe(){
        return this.finVe;
    }

    public Statut getStatut(){
        return this.statut;
    }

    //SETTER

    public void setIdVe(int idV){
        this.idVe=idV;
    }

    public void setObjet(Objet ob){
        this.objet=ob;
    }

    public void setPrixBase(int prixB){
        this.prixBase=prixB;
    }

    public void setPrixMin(int prixM){
        this.prixMin=prixM;
    }

    public void setDebutVe(String debutV){
        this.debutVe=debutV;
    }

    public void setFinVe(String finV){
        this.finVe=finV;
    }

    public void setStatut(Statut st){
        this.statut=st;
    }
}