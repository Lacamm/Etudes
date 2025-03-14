import java.util.HashMap;

class Clone implements FabriqueAnimal {

  private HashMap<String,Integer> NumClone;
  private HashMap<Normal.TYPE,String> TypeClone;

  @Override
  public Animal creerAnimal(Normal.TYPE type, String nom) {
    if (type == Normal.TYPE.PERROQUET){
      return new Perroquet(nom, new Cage());
    }
    else if (type == Normal.TYPE.LION){
      return new Lion(nom, new Enclos());
    }
    else {
      return new Chien(nom,new Libre());
    }
  }
}
