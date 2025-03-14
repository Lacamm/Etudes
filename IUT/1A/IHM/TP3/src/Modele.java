import java.util.Collections;
import java.util.List;

public class Modele {

    private List<Score> scores;
    private int limite;

    public Modele(){
        this.scores = new Score();
        this.limite = 5;
    }

    public int getNbPlaces(){return this.limite-this.scores.size();}

    public int getNbScores(){return this.scores.size();}

    public Integer getScore(int place){return this.scores.get(place).getPoints();}

    public void ajouterScore(String nom, int nbPoints{
        for (int i=0; i<scores.size();i++){
            if(scores.get(i).getPoints()<nbPoints){
                break;
            }
        }
        if(i<limite){
            scores.add(i,new Score(nom, nbPoints));
            if(scores.size()==limite){
                scores.remove(limite);
            }

        }
    }
}
