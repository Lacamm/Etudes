import java.util.*;

public class Utilisateur{
    private int idUt;
    private String pseudoUt, emailUt, mdpUt;
    private Role role;
    private boolean activeUt;
    private List<Objet> listeO;
    private List<Vente> listeV;
    private List<Message> listeMessageEnv, listeMessageRecu;

    public Utilisateur(int idUt, String pseudoUt, String emailUt, String mdpUt, Role role){
        this.idUt=idUt;
        this.pseudoUt=pseudoUt;
        this.emailUt=emailUt;
        this.mdpUt=mdpUt;
        this.role=role;
        this.activeUt=true;
        this.listeO=new ArrayList<>();
        this.listeV=new ArrayList<>();
        this.listeMessageEnv=new ArrayList<>();
        this.listeMessageRecu=new ArrayList<>();
    }

    //GETTER 

    public int getIdUt(){
        return this.idUt;
    }

    public String getPseudoUt(){
        return this.pseudoUt;
    }

    public String getEmailUt(){
        return this.emailUt;
    }

    public String getMdpUt(){
        return this.mdpUt;
    }

    public Role getRole(){
        return this.role;
    }

    public boolean getActiveUt(){
        return this.activeUt;
    }

    public List<Objet> getListeO(){
        return this.listeO;
    }

    public List<Vente> getListeV(){
        return this.listeV;
    }

    public List<Message> getMessageEnv(){
        return this.listeMessageEnv;
    }

    public List<Message> getMessageRecu(){
        return this.listeMessageRecu;
    }

    //SETTER

    public void setIdUt(int idU){
        this.idUt=idU;
    }

    public void setPseudoUt(String pseudo){
        this.pseudoUt=pseudo;
    }

    public void setEmailUt(String email){
        this.emailUt=email;
    }

    public void setMdpUt(String mdp){
        this.mdpUt=mdp;
    }

    public void setRole(Role r){
        this.role=r;
    }

    public void setActiveUt(boolean active){
        this.activeUt=active;
    }

    public void setListeO(List<Objet> l){
        this.listeO=l;
    }

    public void setListeV(List<Vente> l){
        this.listeV=l;
    }

    public void setMessageEnv(List<Message> l){
        this.listeMessageEnv=l;
    }

    public void setMessageRecu(List<Message> l){
        this.listeMessageRecu=l;
    }
}