import java.util.*;

public class Objet{
    private int idO;
    private String nomOb, descriOb;
    private Utilisateur ut;
    private Categorie cat;

    public Objet(int idO, String nomOb, String descriOb, Utilisateur ut, Categorie cat){
        this.idO=idO;
        this.nomOb=nomOb;
        this.descriOb=descriOb;
        this.ut=ut;
        this.cat=cat;
    }

    //GETTER 

    public int getIdO(){
        return this.idO;
    }

    public String getNomOb(){
        return this.nomOb;
    }

    public String getDescriOb(){
        return this.descriOb;
    }

    public Utilisateur getUt(){
        return this.ut;
    }

    public Categorie getCat(){
        return this.cat;
    }

    //SETTER 

    public void setIdO(int idOb){
        this.idO=idOb;
    }

    public void setNomOb(String nomO){
        this.nomOb=nomO;
    }

    public void setDescriOb(String descriO){
        this.descriOb=descriO;
    }

    public void setUt(Utilisateur u){
        this.ut=u;
    }

    public void setCat(Categorie c){
        this.cat=c;
    }
}