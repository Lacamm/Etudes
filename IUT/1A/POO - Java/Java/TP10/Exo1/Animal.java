public class Animal{
    public String nom;
    public boolean blesse;

    public Animal(String nom, boolean blesse){
        this.nom = nom;
        this.blesse = blesse;
    }

    public String getNom(){return this.nom;}
    public boolean getBlesse(){return this.blesse;}

    public void setBlesse(boolean soin){this.blesse=soin;}
}