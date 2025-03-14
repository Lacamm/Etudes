
class Main {

    public Main(){};

    public static void Main(String [] args){
        Zoo zoo = new Zoo();

        FabriqueAnimal fabriqueAnimal = new Normal();

        Animal lion = fabriqueAnimal.creerAnimal(Normal.TYPE.LION, "marcel");
        Animal perroquet = fabriqueAnimal.creerAnimal(Normal.TYPE.PERROQUET, "fabrice");
        Animal chien = fabriqueAnimal.creerAnimal(Normal.TYPE.CHIEN, "rex");


        FabriqueAnimal fabriqueClone = new Clone();


        zoo.addAnimal(lion);
        zoo.addAnimal(perroquet);
        zoo.addAnimal(chien);

        zoo.nourrirAnimaux();

        zoo.blesse(chien);
        zoo.liberte(perroquet);

    }
}
