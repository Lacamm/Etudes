public class Chaine implements Ajoutable<Chaine>{
    private String x;

    public Chaine(String x){
        this.x=x;
    }

    @Override
    public Chaine ajoute(Chaine a){
        Chaine res = new Chaine(this.x+a.x);
        return res;
        }

    public String toString(){
        return this.x;
    }
}