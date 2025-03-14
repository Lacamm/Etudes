
class Perroquet extends Animal {

    private String nom;

    public Perroquet(String nom, Habitat habitat){
        this.nom = nom;
        habitat = habitat;
    }

    public String getNom() {
        return nom;
    }

    @Override
    public void nourrir() {
        super.nourrir();
    }
}
