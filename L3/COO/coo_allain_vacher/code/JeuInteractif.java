import java.util.Scanner;


public class JeuInteractif {

    public static void main(String[] args) {

        // Initialisation des fabriques
        FabriqueGluant fabriqueGluant = new FabriqueGluant();
        FabriqueSquelette fabriqueSquelette = new FabriqueSquelette();
        FabriqueGobelin fabriqueGobelin = new FabriqueGobelin();
        FabriquePaladin fabriquePaladin = new FabriquePaladin();
        FabriqueAssassin fabriqueAssassin = new FabriqueAssassin();
        FabriqueBarbare fabriqueBarbare = new FabriqueBarbare();


        // Création du jeu
        Jeu jeu = new Jeu();
        Contexte contexte = new Contexte(jeu);
        jeu.setMonContexte(contexte);

        // Création d'un donjon
        Donjon donjon1 = new Donjon("Bikini Bottom");
        Piece piece1 = new Piece();
        PNJ patrick = fabriqueGluant.creerPNJ("Patrick");
        PNJ bob = fabriqueGobelin.creerPNJ("Bob");
        PNJ carlos = fabriqueSquelette.creerPNJ("Carlos");
        PNJ krabs = fabriqueSquelette.creerPNJ("Krabs");
        carlos.boss();
        piece1.add_ennemis(patrick);
        piece1.add_ennemis(bob);

        Piece piece2 = new Piece();
        piece2.add_ennemis(carlos);

        donjon1.add_piece(piece1);
        donjon1.add_piece(piece2);

        donjon1.add_loot(new Objet("Epee de diamant", Objet.TYPE.ARME, 0, 5, 0, 5, 0, "Attaque +5"));
        donjon1.add_loot(new Objet("Chaussures de sport", Objet.TYPE.PIEDS, 2, 0, 2, 2, 0, "PV et Défense +2"));

        jeu.add_donjon(donjon1);

        Donjon donjon2 = new Donjon("Donjon de la mort");
        Piece pieced2 = new Piece();
        PNJ hercule = fabriqueGobelin.creerPNJ("Hercule");
        hercule.boss();
        hercule.setForce(50);
        pieced2.add_ennemis(hercule);

        donjon2.add_piece(pieced2);

        donjon2.add_loot(new Objet("Baton des tempetes", Objet.TYPE.ARME, 0, 100, 0, 1, 0, "Attaque + 100"));
        jeu.add_donjon(donjon2);

        Marchand marchand = new Marchand();
        Objet pomme = new Objet("Pomme rouge", Objet.TYPE.CONSOMMABLE,0,0,0,2,2,"Rend 2 PV");

        marchand.addObjet(new Objet("Plastron en fer", Objet.TYPE.BUSTE,5,0,5,5,0,"PV et Defense +5"),15);
        marchand.addObjet(pomme,2);
        marchand.addObjet(pomme,2);
        marchand.addObjet(pomme,2);

        jeu.addMarchand(marchand);

        // Version interactive en ligne de commande
        Scanner jeuInteractif = new Scanner(System.in);

        System.out.println("Bienvenue dans l'aventure, il est temps pour vous de créer votre personnage");
        System.out.println("A tout moment, tapez help afin d'avoir la liste des commandes disponibles");
        System.out.println("A tout moment, tapez exit pour arreter le jeu");

        while (true) {
            if (jeu.getEtatCourant() instanceof CreationPersonnage) {
                System.out.println("Pour créer votre perso, utiliser la commande creer perso");
            }
            System.out.print("=> ");
            String str = jeuInteractif.nextLine();
            if (str.equalsIgnoreCase("help")) {
                if (jeu.getEtatCourant() instanceof CreationPersonnage) {
                    System.out.println("Voici la liste des commandes disponibles :");
                    System.out.println("    - creer perso : permet de creer un personnage");
                } else if (jeu.getEtatCourant() instanceof Menu) {
                    System.out.println("Voici la liste des commandes disponibles :");
                    System.out.println("    - liste donjons : affiche la liste des donjons");
                    System.out.println("    - inventaire : permet de voir l'inventaire");
                    System.out.println("    - utiliser : permet d'utiliser un objet");
                    System.out.println("    - equiper : permet d'équiper un objet");
                    System.out.println("    - desequiper : permet d'enlever un objet");
                    System.out.println("    - jeter : permet de jeter un objet");
                    System.out.println("    - entrer donjon : permet d'entrer dans un donjon");
                    System.out.println("    - entrer boutique : permet d'entrer chez le marchand");
                } else if (jeu.getEtatCourant() instanceof InterieurDonjon) {
                    System.out.println("Voici la liste des commandes disponibles :");
                    System.out.println("    - inventaire : permet de voir l'inventaire");
                    System.out.println("    - utiliser : permet d'utiliser un objet");
                    System.out.println("    - equiper : permet d'équiper un objet");
                    System.out.println("    - desequiper : permet d'enlever un objet");
                    System.out.println("    - jeter : permet de jeter un objet");
                    System.out.println("    - piece suivante : permet d'entrer dans la piece suivante du donjon");
                    System.out.println("    - fuir : permet de sortir du donjon");
                } else if (jeu.getEtatCourant() instanceof Boutique) {
                    System.out.println("Voici la liste des commandes disponibles :");
                    System.out.println("    - inventaire : permet de voir l'inventaire");
                    System.out.println("    - utiliser : permet d'utiliser un objet");
                    System.out.println("    - equiper : permet d'équiper un objet");
                    System.out.println("    - desequiper : permet d'enlever un objet");
                    System.out.println("    - jeter : permet de jeter un objet");
                    System.out.println("    - boutique : permet de voir la boutique");
                    System.out.println("    - acheter : permet d'acheter un objet de la boutique");
                    System.out.println("    - ameliorer : permet d'ameliorer un de vos objets");
                    System.out.println("    - sortir boutique : permet de sortir de la boutique");
                } else if (jeu.getEtatCourant() instanceof Combat) {
                    System.out.println("Voici la liste des commandes disponibles :");
                    System.out.println("    - attaquer : permet d'attaquer un ennemi");
                }
            } else if (str.equalsIgnoreCase("creer perso")) {
                System.out.println("Vous avez le choix entre 3 classes, Barbare, Assassin ou Paladin");
                System.out.print("Saisir la classe : ");
                String classe = jeuInteractif.nextLine();
                if (classe.equalsIgnoreCase("Assassin") || classe.equalsIgnoreCase("Paladin") || classe.equalsIgnoreCase("Barbare")) {
                    System.out.print("Saisir le nom du personnage : ");
                    String nom = jeuInteractif.nextLine();
                    if (classe.equalsIgnoreCase("Assassin")) {
                        jeu.eventCreationPersonnage(nom, fabriqueAssassin);
                    } else if (classe.equalsIgnoreCase("Paladin")) {
                        jeu.eventCreationPersonnage(nom, fabriquePaladin);
                        jeu.getPersonnage().setArgent(100);
                    } else if (classe.equalsIgnoreCase("Barbare")) {
                        jeu.eventCreationPersonnage(nom, fabriqueBarbare);
                    }
                } else {
                    System.out.println("Le nom de la classe n'est pas valide");
                }
            } else if (str.equalsIgnoreCase("entrer donjon")) {
                System.out.print("Quel est le nom du donjon que vous voulez rejoindre ? : ");
                str = jeuInteractif.nextLine();
                jeu.eventEntrerDonjon(str);
            } else if (str.equalsIgnoreCase("attaquer")) {
                System.out.print("Quel est le nom du monstre que vous souhaitez attaquer ? : ");
                str = jeuInteractif.nextLine();
                jeu.eventAttaque(str);
            } else if (str.equalsIgnoreCase("inventaire")) {
                jeu.eventVoirInventaire();
            } else if (str.equalsIgnoreCase("utiliser")) {
                System.out.print("Quel est le nom de l'objet que vous souhaitez utiliser ? : ");
                str = jeuInteractif.nextLine();
                jeu.eventConsommer(str);
            } else if (str.equalsIgnoreCase("equiper")) {
                System.out.print("Quel est le nom de l'objet que vous souhaitez équiper ? : ");
                str = jeuInteractif.nextLine();
                jeu.eventEquiper(str);
            } else if (str.equalsIgnoreCase("desequiper")) {
                System.out.print("Quel est le nom de l'objet que vous souhaitez desequiper ? : ");
                str = jeuInteractif.nextLine();
                jeu.eventDesequiper(str);
            } else if (str.equalsIgnoreCase("jeter")) {
                System.out.print("Quel est le nom de l'objet que vous souhaitez jeter ? : ");
                str = jeuInteractif.nextLine();
                jeu.eventJeter(str);
            } else if (str.equalsIgnoreCase("entrer boutique")) {
                jeu.eventEntrerMarchand();
            } else if (str.equalsIgnoreCase("boutique")) {
                jeu.eventVoirBoutique();
            } else if (str.equalsIgnoreCase("acheter")) {
                System.out.print("Quel est le nom de l'objet que vous souhaitez acheter ? : ");
                str = jeuInteractif.nextLine();
                jeu.eventAcheter(str);
            } else if (str.equalsIgnoreCase("ameliorer")) {
                System.out.print("Quel est le nom de l'objet que vous souhaitez améliorer ? : ");
                str = jeuInteractif.nextLine();
                jeu.eventAmeliorer(str);
            } else if (str.equalsIgnoreCase("liste donjons")) {
                jeu.eventVoirMenu();
            } else if (str.equalsIgnoreCase("sortir boutique")) {
                jeu.eventSortieMarchand();

            } else if (str.equalsIgnoreCase("piece suivante")) {
                jeu.eventPieceSuivante();
            }else if (str.equalsIgnoreCase("fuir")) {
                System.out.println("Si vous sortez maintenant, vous allez perdre votre progression, êtes-vous sur ?");
                str = jeuInteractif.nextLine();
                if (str.equalsIgnoreCase("Oui"))
                    jeu.eventQuitterDonjon();
            }else if(str.equalsIgnoreCase("exit")){
                System.out.println("Voulez vous vraiment fermer le jeu ?");
                str = jeuInteractif.nextLine();
                if (str.equalsIgnoreCase("Oui"))
                    break;
            }
            else
                System.out.println("Commande inconnue");
        }
    }
}
