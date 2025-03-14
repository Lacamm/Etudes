import java.util.*;

public class Etudiant implements Comparable<Etudiant>{
    private String nom, prenom;
    private int telepathie, precognition, telekinesie;

    public Etudiant(String nom, String prenom){
        this.nom = nom;
        this.prenom = prenom;
        this.telekinesie = -1;
        this.telepathie = -1;
        this.precognition = -1;
    }

    public Etudiant(String nom, String prenom, int telekinesie, int telepathie, int precognition){
        this.nom = nom;
        this.prenom = prenom;
        this.telekinesie = telekinesie;
        this.telepathie = telepathie;
        this.precognition = precognition;
    }

    public int getTelepathie(){return this.telepathie;}
    public int getTelekinesie(){return this.telekinesie;}
    public int getPrecognition(){return this.precognition;}

    public void setPrecognition(int val){this.precognition = val;}
    public void setTelekinesie(int val){this.telekinesie = val;}
    public void setTelepathie(int val){this.telepathie = val;}

    @Override
    public boolean equals(Object o){
        if (o instanceof Etudiant){
            return this.nom.equals(((Etudiant) o).nom) && this.prenom.equals(((Etudiant) o).prenom);
        }
        return false;
    }

    @Override
    public int hashCode(){
        return Objects.hash(this.nom, this.prenom);
    }

    @Override
    public String toString(){
        if (this.telekinesie == -1 || this.telepathie == -1 || this.precognition == -1){
            return this.prenom+" "+this.nom+" - Il manque des notes";
        }
        else{
            return this.prenom+" "+this.nom+" - Notes : télépathie="+this.telepathie+" précognition="+this.precognition+" télékinésie="+this.telekinesie;
        }
    }

    @Override

    public int compareTo(Etudiant etu){
        return etu.telekinesie - this.telekinesie;
    }
}