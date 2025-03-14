import java.util.ArrayList;

class Normal implements FabriqueAnimal {

    public enum TYPE {PERROQUET,CHIEN,LION};

    @Override
    public Animal creerAnimal(TYPE type, String nom) {
        if (type == TYPE.PERROQUET){
            return new Perroquet(nom, new Cage());
        }
        else if (type == TYPE.LION){
            return new Lion(nom, new Enclos());
        }
        else {
            return new Chien(nom,new Libre());
        }
    }
}
