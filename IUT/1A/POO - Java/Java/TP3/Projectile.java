public class Projectile {

    double positionX,positionY;

    public void Projectile(double positionX, double positionY){
        this.positionX = positionX;
        this.positionY = positionY;
    }
    public EnsembleChaines getEnsembleChaines(){
        EnsembleChaines ens = new EnsembleChaines();
        int pos1 = (int) this.positionX;
        int pos2 = (int) this.positionY;
        ens.ajouteChaine(pos1,pos2,"^");
        return ens;
    }
    public void evolue(){
        this.positionY += 0.2;
    }
}