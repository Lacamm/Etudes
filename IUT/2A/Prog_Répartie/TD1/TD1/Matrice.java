import java.util.ArrayList;

public class Matrice {
    
    private ArrayList<Integer> chiffres;
    private int largeur;

    public Matrice(ArrayList<Integer> chiffres, int largeur){
        this.largeur = largeur;
        this.chiffres = chiffres;
    }

    public Matrice multiplier(Matrice matrice2) throws InterruptedException {
        ArrayList<Multiplication> multiplications = new ArrayList<>();
        for (int i = 0; i!= this.chiffres.size(); i++){
            Multiplication m = new Multiplication(this.chiffres.get(i), matrice2.getChiffres().get((int)(Math.floor(i/this.largeur) *this.largeur + i%this.largeur)));
            multiplications.add(m);
        }
        ThreadTest t1 = new ThreadTest();
        ThreadTest t2 = new ThreadTest();
        for (int i = 0; i< (multiplications.size()/2)-1; i++){
            t1.ajoutMultiplication(multiplications.get(i));
            t2.ajoutMultiplication(multiplications.get(multiplications.size()-i-1));
        }
        t1.start();
        t2.start();

        t1.join();
        t2.join();

        ArrayList<Integer> valeurs = new ArrayList<>();
        for (int i = 0; i!= multiplications.size(); i++){
            valeurs.add(multiplications.get(i).getResultat());
        }

        return new Matrice(valeurs, this.largeur);
    }

    public ArrayList<Integer> getChiffres(){
        return this.chiffres;
    }
    @Override
    public String toString(){
        String res = "";
        for (Integer val: this.chiffres){
            res+=val.toString()+" ";
        }
        return res;
    }
}
