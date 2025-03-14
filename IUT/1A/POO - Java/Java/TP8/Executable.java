import java.util.List;
import java.util.ArrayList;
import java.lang.Math; 
public class Executable {
    public static void main(String [] args) {
	System.out.println("Entier et Ajoutable"); 
	Entier cinq = new Entier(5);
	Entier trois = new Entier(3);
	System.out.println(cinq.ajoute(trois));
	
	System.out.println("Ajoutables et Entier"); 
	List<Entier> lE = new ArrayList<>();
	lE.add(trois);
	lE.add(cinq);
	lE.add(new Entier(2));
	lE.add(cinq);
	lE.add(new Entier(-3));
	lE.add(new Entier(10));
	lE.add(cinq);
	System.out.println(Ajoutables.somme(lE));
	
	System.out.println("Ajoutables et Chaine");
	List<Chaine> lCh = new ArrayList<>();
	lCh.add(new Chaine("a"));
	lCh.add(new Chaine("u"));
	lCh.add(new Chaine("jour"));
	lCh.add(new Chaine("d hui"));
	lCh.add(new Chaine("!!"));
	System.out.println(Ajoutables.somme(lCh));
	/*
	
	System.out.println("Element majoritaire");
	List<Integer> lEM = new ArrayList<>();
	for(int i = 0; i < 1000000; ++i)
	    lEM.add((int)(Math.random()*100));
	System.out.println(ElementMajoritaire.elementMajoritaire(lEM)); 
	System.out.println("Element majoritaire Générique");
	List<Integer> lEMG = new ArrayList<>();
	for(int i = 0; i < 1000000; ++i)
	    lEMG.add((int)(Math.random()*100));
	System.out.println(ElementMajoritaireE.elementMajoritaire(lEMG));
	List<Integer> lIE = new ArrayList<>();
	lIE.add(-1);
	lIE.add(1);
	lIE.add(5);
	lIE.add(7);
	lIE.add(11); 
	System.out.println(IndiceEgal.indiceEgal(lIE));
	List<Integer> lIE1 = new ArrayList<>();
	lIE1.add(-1);
	lIE1.add(2);
	lIE1.add(5);
	lIE1.add(7);
	lIE1.add(11); 
	System.out.println(IndiceEgal.indiceEgal(lIE1)); 
	*/ 
    }
}
