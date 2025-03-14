public class Score {
    private String nom;
    private Integer points;

    public Score(String nom, Integer points){
        this.nom = nom;
        this.points = points;
    }

    public String getNom(){return this.nom;}
    public Integer getPoints(){return this.points;}

}
