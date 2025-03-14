public class Entier implements Ajoutable<Entier>{
    private Integer x;

    public Entier(Integer x){
        this.x=x;
    }

    @Override
    public Entier ajoute(Entier a){
        Entier res = new Entier(this.x+a.x);
        return res;
        }

    public String toString(){
        return ""+this.x;
    }
}