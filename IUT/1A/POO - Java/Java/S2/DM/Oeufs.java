public class Oeufs{
    private String type;
    private int poids;
    private int nombre_d_oeufs;

    public Oeufs(String type, int poids){
        this.type = type;
        this.poids = poids;
        this.nombre_d_oeufs = 0;
    }

    public Oeufs(String type, int poids, int nombre){
        this.type = type;
        this.poids = poids;
        nombre_d_oeufs = nombre;
    }

    // Getters
    public String getType(){return this.type;}
    public int getPoids(){return this.poids;}
    public int getNombre(){return this.nombre_d_oeufs;}

    //Setter
    public void ajouteOeufs(int nombre){this.nombre_d_oeufs += nombre;}

    public String toString(){
        String res;
        res = this.nombre_d_oeufs+" oeufs au chocolat "+this.type+" de "+this.poids+" grammes.";
        return res;
    }
}