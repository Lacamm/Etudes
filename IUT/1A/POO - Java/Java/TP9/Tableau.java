import java.util.List;
import java.util.ArrayList;
import java.lang.Math;
import java.util.NoSuchElementException;
import java.util.Collections;

public class Tableau {
    private List<Integer> tab;

    public Tableau () {tab = new ArrayList<Integer>();}

    public void remplir() {
        int nb = (int)(Math.random()* 10);
        for(int i = 0; i< nb; ++i)
            this.tab.add((int)(Math.random()* 50));
    }

    public List<Integer> getContenu(){return this.tab;}

    public Integer get(Integer indice)throws NoSuchElementException{
        if (indice < 0 || indice > this.tab.size()-1){
            throw new NoSuchElementException();
        }
        return this.tab.get(indice);
    }

   public Integer getMax()throws NoSuchElementException{
       if (!this.tab.isEmpty()){
           return Collections.max(this.tab);
       }
       throw new NoSuchElementException();
   }

    public Integer getMin()throws NoSuchElementException{
        if (!this.tab.isEmpty()){
           return Collections.min(this.tab);
       }
       throw new NoSuchElementException();
    }

   public String toString() {return tab.toString();}
}