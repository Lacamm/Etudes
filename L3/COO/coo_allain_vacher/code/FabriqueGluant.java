
public class FabriqueGluant implements FabriquePNJ {
    @Override
    public PNJ creerPNJ(String nom){
        return new Gluant(nom);
    }
}
