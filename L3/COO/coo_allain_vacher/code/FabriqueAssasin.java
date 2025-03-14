public class FabriqueAssasin implements FabriquePersonnage {
    @Override
    public Personnage creerPersonnage(String nom){
        return new Assassin(nom);
    }
}