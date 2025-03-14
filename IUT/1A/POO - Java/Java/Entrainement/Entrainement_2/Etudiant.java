import java.util.*;

public class Etudiant{

    private String nom,prenom;
    private int telek, telep, preco;

    public Etudiant(String nom, String prenom){
        this.nom = nom;
        this.prenom = prenom;
        this.telek = null;
        this.telep = null;
        this.preco = null;
    }

    public Etudiant(String nom, String prenom, int telep, int preco, int telek){
        this.nom = nom;
        this.prenom = prenom;
        this.telek = telek;
        this.telep = telep;
        this.preco = preco;
    }

    public int getTelep(){return this.telep;}
    public void setPreco(int val){this.preco = val;}

    @Override
    public String toString(){
        if(this.preco == null || this.telek == null || this.telep == null){
            return this.prenom+" "+this.nom+" - Il manque des notes.";
        }
        else{
            return this.prenom+" "+this.nom+" - Notes : télépathie="+this.telep+" précognition="+this.preco+" télékinésie"+this.telek;
        }
    }

    @Override
    public int hashCode(){return Objects.hash(this.nom, this.prenom);}
}