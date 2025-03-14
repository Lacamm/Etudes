public class Score {
    private String nom;
    private int score;
    public Score(String nom, int score){
        this.nom = nom;
        this.score = score;
    }
    public int getScore(){
        return this.score;
    }

    public String toString(){
        return this.nom+' '+this.score;
    }
}
