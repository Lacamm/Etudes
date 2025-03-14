import java.util.Scanner;

public class InterfaceJeu {

  public static void main(String[] args)
  {
    // Initialisation des fabriques
    FabriquePNJ fabriqueGluant = new FabriqueGluant();
    FabriquePNJ fabriqueSquelette = new FabriqueSquelette();
    FabriquePNJ fabriqueGobelin = new FabriqueGobelin();
    FabriquePersonnage fabriquePaladin = new FabriquePaladin();
    FabriquePersonnage fabriqueAssassin = new FabriqueAssassin();
    FabriquePersonnage fabriqueBarbare = new FabriqueBarbare();


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

    donjon1.add_loot(new Objet("Epee de diamant", Objet.TYPE.ARME,0,5,0,5,0,"Attaque +5"));
    donjon1.add_loot(new Objet("Chaussures de sport", Objet.TYPE.PIEDS,2,0,2,2,0,"PV et Défense +2"));

    jeu.add_donjon(donjon1);

    Donjon donjon2 = new Donjon("Donjon de la mort");
    Piece pieced2 = new Piece();
    PNJ hercule = fabriqueGobelin.creerPNJ("Hercule");
    hercule.boss();
    hercule.setForce(50);
    pieced2.add_ennemis(hercule);

    donjon2.add_piece(pieced2);

    donjon2.add_loot(new Objet("Baton des tempetes",Objet.TYPE.ARME,0,100,0,1,0,"Attaque + 100"));
    jeu.add_donjon(donjon2);

    Marchand marchand = new Marchand();
    Objet pomme = new Objet("Pomme rouge", Objet.TYPE.CONSOMMABLE,0,0,0,2,2,"Rend 2 PV");

    marchand.addObjet(new Objet("Plastron en fer", Objet.TYPE.BUSTE,5,0,5,5,0,"PV et Defense +5"),15);
    marchand.addObjet(pomme,2);
    marchand.addObjet(pomme,2);
    marchand.addObjet(pomme,2);

    jeu.addMarchand(marchand);

    // Création d'un personnage
    jeu.eventCreationPersonnage("Valentin",fabriquePaladin);

    // Deroulement du jeu

    jeu.eventEquiper("Epee en pierre");
    jeu.eventEquiper("Casque en cuir");


    jeu.eventVoirInventaire();

    jeu.eventEntrerDonjon("Bikini Bottom");


    jeu.eventAttaque("Patrick");
    jeu.eventAttaque("Patrick");
    jeu.eventAttaque("Bob");
    jeu.eventAttaque("Bob");
    jeu.eventAttaque("Bob");

    jeu.eventConsommer("Potion de vie superieure");
    jeu.eventPieceSuivante();

    jeu.eventAttaque("Carlos");
    jeu.eventAttaque("Carlos");
    jeu.eventAttaque("Carlos");
    jeu.eventPieceSuivante();

    jeu.eventVoirInventaire();

    jeu.eventEquiper("Epee de diamant");
    jeu.eventEquiper("Chaussures de sport");

    jeu.eventVoirInventaire();

    jeu.eventEntrerMarchand();
    jeu.eventVoirBoutique();

    jeu.eventAcheter("Pomme rouge");

    jeu.eventAmeliorer("Epee de diamant");

    jeu.eventSortieMarchand();

    jeu.eventEntrerDonjon("Donjon de la mort");
    jeu.eventAttaque("Hercule");

    jeu.eventVoirInventaire();

    jeu.eventJeter("Potion de vie");

    jeu.eventVoirInventaire();

  }
}
