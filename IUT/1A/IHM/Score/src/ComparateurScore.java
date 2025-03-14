import java.util.Comparator;

public class ComparateurScore implements Comparator<Score>{

  public int compare(Score s1, Score s2){
      return s2.getScore()-s1.getScore();
  }
}
