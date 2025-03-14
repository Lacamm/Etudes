
class Chien extends Animal {

    private String nom;

    public Chien(String nom, Habitat habitat){
        this.nom = nom;
        habitat = habitat;
    }

    @Override
    public void nourrir() {
        super.nourrir();
    }
}
