import java.util.*;

public class Document{
    private int idD;
    private String titreDoc;
    private byte[] contenuDoc;
    private String dateDoc;
    private Utilisateur ut;
    private Objet objet;

    public Document(int idD, String titreDoc, byte[] contenuDoc, String dateDoc, Utilisateur ut, Objet objet){
        this.idD=idD;
        this.titreDoc=titreDoc;
        this.contenuDoc=contenuDoc;
        this.dateDoc=dateDoc;
        this.ut=ut;
        this.objet=objet;
    }

    //GETTER 

    public int getIdD(){
        return this.idD;
    }

    public String getTitreDoc(){
        return this.titreDoc;
    }

    public byte[] getContenuDoc(){
        return this.contenuDoc
    }

    public String getDateDoc(){
        return this.dateDoc
    }

    public Utilisateur getUt(){
        return this.ut;
    }

    public Objet getObjet(){
        return this.objet;
    }

    //SETTER 

    public void setIdD(int id){
        this.idD=id;
    }

    public void setTitreDoc(String titre){
        this.titreDoc=titre;
    }

    public void setContenuDoc(byte[] cont){
        this.contenuDoc=cont;
    }

    public void setDateDoc(String date ){
        this.dateDoc=date;
    }

    public void setUt(Utilisateur u){
        this.ut=u;
    }

    public void setObjet(Objet ob){
        this.objet=ob;
    }

}