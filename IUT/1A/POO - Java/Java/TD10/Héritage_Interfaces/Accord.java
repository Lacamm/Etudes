import java.util.*;
import java.lang.*;

public class Accord extends HasSet<Note>{

    public int duree(){
        int max=0;
        for(Note n:this){
            if(n.getDuree() > max){
                max = n.getDuree();
            }
        }
        return max;
    }

    public boolean estHarmonieux(){
        boolean res = true;
        for(Note n:this){
            if (n.getFrequence()%2 !=0){
                res = false;
            } 
        }
        return res;
    }

    public static boolean estPuissanceDeux(Note note){
        boolean res = true;
    }

    public String jouer(){
        System.out.println("je joue un accord   ");
        for(Note n: this){
            n.jouer();
            System.out.println("  -  ");
        }
        System.out.println();
    }

}