import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class Scores {
    private List<Score> listeScore;
    private int tailleMax;

    public Scores(int tailleMax){
        this.tailleMax = tailleMax;
        this.listeScore = new ArrayList<>();
    }

    public boolean ajouterScore(String nom, int score){
        if(this.listeScore.size() < this.tailleMax) {
            this.listeScore.add(new Score(nom, score));
            Collections.sort(this.listeScore,new ComparateurScore());
            return true;
        }
        else{
            Collections.sort(this.listeScore,new ComparateurScore());
            if(score>this.listeScore.get(listeScore.size()-1).getScore()){
                this.listeScore.remove(listeScore.size()-1);
                this.listeScore.add(new Score(nom, score));
                Collections.sort(this.listeScore,new ComparateurScore());
                return true;
            }
        return false;
        }
    }

    public String getScores(int position){
        return this.listeScore.get(position).toString();
    }

    public int getNbPlaces(){
        return this.tailleMax-this.listeScore.size();
    }

    public int getNbScore(){
        return this.listeScore.size();
    }

    public List<Score> getliste(){
        return this.listeScore;
    }
}
