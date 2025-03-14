
public class FabriqueGobelin implements FabriquePNJ {
    @Override
    public PNJ creerPNJ(String nom){
        return new Gobelin(nom);
    }
}
