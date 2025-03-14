import java.util.*;

public class Message{
    private boolean luMsg;
    private int idMsg;
    private Utilisateur exp,dest;
    private String dateMsg,contenuMsg;
    private Objet objet;

    public Message(int idMsg, String dateMsg, String contenuMsg, Utilisateur exp, Utilisateur dest, Objet objet){
        this.idMsg=idMsg;
        this.dateMsg=dateMsg;
        this.contenuMsg=contenuMsg;
        this.dest=dest;
        this.exp=exp;
        this.objet=objet;
        this.luMsg=false;
    }

    //GETTER 

    public int getIdMsg(){
        return this.idMsg;
    }

    public String getDateMsg(){
        return this.dateMsg;
    }

    public String getDontenuMsg(){
        return this.contenuMsg;
    }

    public Utilisateur getDest(){
        return this.dest;
    }

    public Utilisateur getExp(){
        return this.exp;
    }

    public Objet getObjet(){
        return this.objet;
    }

    public boolean getLuMsg(){
        return this.luMsg;
    }

    //SETTER 

    public void setIdMsg(int id){
        this.idMsg=id;
    }

    public void setDateMsg(String d){
        this.dateMsg=d;
    }

    public void setContenuMsg(String msg){
        this.contenuMsg=msg;
    }

    public void setDest(Utilisateur u){
        this.dest=u;
    }

    public void setExp(Utilisateur u){
        this.exp=u;
    }

    public void setObjet(Objet ob){
        this.objet=ob;
    }
    public void setLuMsg(boolean b){
        this.luMsg=b;
    }

    
    


}