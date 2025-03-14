public class Executable {
    public static void main(String [] args) {

    Etudiant luke = new Etudiant("Luke", "Skywalker", 2, 8, 14);
    System.out.println(luke);
    // Luke Skywalker - Notes : télépathie=2 précognition=8 télékinésie=14

    Etudiant leia = new Etudiant("Leia", "Organa");
    System.out.println(leia);
    // Leia Organa - Il manque des notes

    leia.setTelepathie(15);
    System.out.println(leia);
    // Leia Organa - Il manque des notes
    
    leia.setTelekinesie(12);
    leia.setPrecognition(17);
    System.out.println(leia);
    // Leia Organa - Notes : télépathie=15 précognition=17 télékinésie=12
    }
}