import java.util.ArrayList;


class Zoo {
  private ArrayList<Animal> mesAnimaux = new ArrayList<Animal>();

  public void nourrirAnimaux() {
    for (Animal animal : mesAnimaux){
      animal.nourrir();
    }
  }

  public void addAnimal(Animal a) {
    mesAnimaux.add(a);
  }

  public void blesse(Animal a) {
    a.setMonHabitat(new Cage());
    System.out.println(a.getNom() + "est bléssé");
  }

  public void liberte(Animal a) {
    a.setMonHabitat(new Libre());
    System.out.println(a.getNom() + " est désormais libre");
  }

}
