public class Couple implements Contenant<Integer>{
    private Integer x,y;

    public Couple(Integer x, Integer y){
        this.x = x;
        this.y = y;
    }

    public boolean contient(Integer X){
        boolean res;
        res = false;
        if (X.equals(this.x) || X.equals(this.y)){
            res = true;
        }
        return res;
    }
}
