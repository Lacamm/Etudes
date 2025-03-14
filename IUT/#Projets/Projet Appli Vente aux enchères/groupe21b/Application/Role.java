import java.util.*;

public class Role{
    private int idRole;
    private String nomRole;

    public Role(int idRole, String nomRole){
        this.idRole=idRole;
        this.nomRole=nomRole;
    }

    //GETTER

    public int getIdRole(){
        return this.idRole;
    }

    public String getNomRole(){
        return this.nomRole;
    }

    //SETTER

    public void setIdRole(int idR){
        this.idRole=idR;
    }

    public void setNomRole(String nomR){
        this.nomRole=nomR;
    }
}