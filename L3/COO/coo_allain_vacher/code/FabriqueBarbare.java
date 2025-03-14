public class FabriqueBarbare implements FabriquePersonnage {
    @Override
    public Personnage creerPersonnage(String nom){
        return new Barbare(nom);
    }
}