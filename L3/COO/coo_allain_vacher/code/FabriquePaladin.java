
public class FabriquePaladin implements FabriquePersonnage {
    @Override
    public Personnage creerPersonnage(String nom){
        return new Paladin(nom);
    }
}
