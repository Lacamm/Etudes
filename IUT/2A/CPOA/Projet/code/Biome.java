
import java.util.*;

public class Biome {

  //
  // Fields
  //
  public static List<Prairies> lPrairies = new ArrayList<>();
  public static List<Nourriture> lNPrairies = new ArrayList<>();

  //
  // Methods
  //
    public static List<Prairies> getPrairie(){
      return lPrairies;
  }


  public static void addPrairies(Prairies p){
    lPrairies.add(p);
  }


  public static void addNPrairies(Nourriture n){
    lNPrairies.add(n);
  }

  public static void removeNPrairies(Nourriture n){
    lNPrairies.remove(n);
  }

  public static void addAnimal(Animal a1, Prairies p1){
    p1.addEspece(a1);
  }


  //
  // Accessor methods
  //

  public String toString(){
    return "Nombre prairies:"+lPrairies.size()+"\n";
  }

}
