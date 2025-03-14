
public class FabriqueSquelette implements FabriquePNJ{

    @Override
    public PNJ creerPNJ(String nom){
        return new Squelette(nom);
    }
}
