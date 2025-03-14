import java.util.List;
import java.util.ArrayList;

public class Zoo{
    public String nom;
    public List<Animal> listeAnimaux;

    public Zoo(String nom){
        this.nom = nom;
        this.listeAnimaux = new ArrayList<>();
    }

    public void acceuillir(Animal animal){
        this.listeAnimaux.add(animal);
    }

    public void soigner(Animal animal)throws AnimalPasPresentException, AnimalPasBlesseException{
        boolean animalPresent;
        animalPresent = false; 
        for (Animal a: listeAnimaux){
            if (animal.getNom().equals(a.getNom())){
                animalPresent = true;
            }
        }
        if (! animalPresent){
            throw new AnimalPasPresentException();
        }
        else{
            if (animal.getBlesse()){
                animal.setBlesse(false);
            }
            else{throw new AnimalPasBlesseException();}
        }
    }
}

