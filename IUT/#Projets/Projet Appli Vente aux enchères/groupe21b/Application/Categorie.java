import java.util.*;

public class Categorie{
    private int idCat;
    private String nomCat;

    public Categorie(int idCat, String nomCat){
        this.idCat=idCat;
        this.nomCat=nomCat;
    }

    //GETTER

    public int getIdCat(){
        return this.idCat;
    }

    public String getNomCat(){
        return this.nomCat;
    }

    //SETTER

    public void setIdCat(int idC){
        this.idCat=idC;
    }

    public void setNomCat(String nomC){
        this.nomCat=nomC;
    }
}