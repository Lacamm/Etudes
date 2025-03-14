
class Lion extends Animal {

    private String nom;

    public Lion(String nom, Habitat habitat){
        this.nom = nom;
        habitat = habitat;
    }

    public String getNom() {
        return this.nom;
    }

    @Override
    public void nourrir() {
        super.nourrir();
    }

}
