import java.util.*;

public class Photo{
    private int idPhoto;
    private Objet objet;
    private String titrePh;
    private byte[] imgPh;

    public Photo(int idPhoto, Objet objet, String titrePh, byte[] imgPh ){
        this.idPhoto=idPhoto;
        this.objet=objet;
        this.titrePh=titrePh;
        this.imgPh=imgPh;
    }

    //GETTER

    public int getIdPhoto(){
        return this.idPhoto;
    }

    public Objet getObjet(){
        return this.objet;
    }

    public String getTitrePh(){
        return this.titrePh;
    }

    public byte[] getImgPh(){
        return this.imgPh;
    }

    //SETTER

    public void setIdPhoto(int idP){
        this.idPhoto=idP;
    }

    public void setObjet(Objet ob){
        this.objet=ob;
    }

    public void setTitrePh(String titre){
        this.titrePh=titre;
    }

    public void setImgPh(byte[] img){
        this.imgPh=img;
    }



}