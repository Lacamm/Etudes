import java.util.*;

public class Statut{
    private int idSt;
    private String nomSt;

    public Statut(int idSt, String nomSt){
        this.idSt=idSt;
        this.nomSt=nomSt;
    }

    //GETTER

    public int getIdSt(){
        return this.idSt;
    }

    public String getNomSt(){
        return this.nomSt;
    }

    //SETTER

    public void setIdSt(int idS){
        this.idSt=idS;
    }

    public void setNomSt(String nomS){
        this.nomSt=nomS;
    }
}