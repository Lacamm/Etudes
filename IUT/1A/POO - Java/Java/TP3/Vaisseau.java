public class Vaisseau {

    private double posX;

    public void Vaisseau(){
        this.posX = 0;
    }

    public void deplace(double dx){
        this.posX += dx;
    }

    public EnsembleChaines getEnsembleChaines(){
        EnsembleChaines ens = new EnsembleChaines();
        int pos = (int) this.posX;
        ens.ajouteChaine(pos,0,"█████████████");
        ens.ajouteChaine(pos,1,"▄███████████▄");
        ens.ajouteChaine(pos+5,2,"███");
        ens.ajouteChaine(pos+6,3,"▄");
        return ens;
    }

    public void positionCanon(){
        this.posX += 6;
    }
}