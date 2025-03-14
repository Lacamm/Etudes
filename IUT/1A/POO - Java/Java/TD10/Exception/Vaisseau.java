public class Vaisseau{

    private int position=15;
    private int nb_projectiles=10;
    private int nb_point_de_vie=5;

    public void deplacer(int deplacement)throws DeplacementImpossible{
        if(this.position + deplacement < 0){
            throw new DeplacementImpossible();
        }
        else{
            this.position+=deplacement;
        }
    }

    public void tirer() throws PlusDeProjectilesException{
        if (this.nb_projectiles<=0){
            throw new PlusDeProjectilesException();
        }
        else{
            this.nb_projectiles-=1;
        }

    public void retirerVie()

    }
}