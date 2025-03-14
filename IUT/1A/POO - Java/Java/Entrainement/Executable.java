import java.util.*;

class Executable {
    public static void main(String [] args) {

        Etudiant luke = new Etudiant("Luke", "Skywalker", 2, 8, 14);
        // System.out.println(luke);
        // // Luke Skywalker - Notes : télépathie=2 précognition=8 télékinésie=14
        
        // Etudiant leia = new Etudiant("Leia", "Organa");
        // System.out.println(leia);
        // // Leia Organa - Il manque des notes
        // leia.setTelepathie(15);
        // System.out.println(leia);
        // // Leia Organa - Il manque des notes
        // leia.setTelekinesie(12);
        // leia.setPrecognition(17);
        // System.out.println(leia);
        // // Leia Organa - Notes : télépathie=15 précognition=17 télékinésie=12

        // List<Etudiant> lesEtu = new ArrayList<>();

        Etudiant solo = new Etudiant("Han", "Solo", 15, 10, 10);
        Etudiant chewie = new Etudiant("Chewbaka", "WaoWaaoWaooo", 2, 11, 18);
        Etudiant yoda = new Etudiant("Maitre", "Yoda", 13, 15, 20);
        List<Etudiant> listeEtudiants = Arrays.asList(luke, solo, chewie, yoda);
        Etablissement ecoleDesMines = new BTP("Ecole des Mines",3);
        System.out.println(ecoleDesMines.getSelection(listeEtudiants));
        //[(Maitre Yoda : télépathie = 13 précognition = 15 télékinésie = 20),
        // (Chewbaka WaoWaaoWaooo : télépathie = 2 précognition = 11 télékinésie = 18),
        // (Luke Skywalker : télépathie = 2 précognition = 8 télékinésie = 14),
        // (Han Solo : télépathie = 15 précognition = 10 télékinésie = 10)]
        Etablissement sciencePo = new Politique("Science Po");
        System.out.println(sciencePo.getSelection(listeEtudiants));
        // [(Maitre Yoda : télépathie = 13 précognition = 15 télékinésie = 20),
        // (Han Solo : télépathie = 15 précognition = 10 télékinésie = 10),
        // (Chewbaka WaoWaaoWaooo : télépathie = 2 précognition = 11 télékinésie = 18),
        // (Luke Skywalker : télépathie = 2 précognition = 8 télékinésie = 14)]
    }
}
