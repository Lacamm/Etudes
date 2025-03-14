public class Fantome{
    private String nom, origine;
    private int nuisance;

    public Fantome(String nom, String origine, int nuisance){
        this.nom = nom;
        this.origine = origine;
        this.nuisance = nuisance;
    }
    public Fantome(String nom, String origine){
        this.nom = nom;
        this.origine = origine;
        this.nuisance = -1;
    }

    public int getNuisance(){
        return this.nuisance;
    }

    public String toString(){
        if(this.nuisance != -1){
            return this.nom+" fantôme "+this.origine+" de nuisance "+this.nuisance+". ";
        }
        else{
            return this.nom+" fantôme "+this.origine+". ";
        }
    }
}