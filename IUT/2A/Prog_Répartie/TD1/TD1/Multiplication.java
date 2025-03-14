public class Multiplication {
    private int a,b,resultat;

    public Multiplication(int a, int b){
        this.a = a;
        this.b = b;
    }

    public void multiplier(){
        this.resultat = this.a*this.b;
    }

    public int getResultat(){
        return this.resultat;
    }

}
