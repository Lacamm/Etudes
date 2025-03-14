import jdk.jfr.ContentType;

import javax.naming.Context;

public interface EtatJeu {

  void gererEntreeDonjon(Contexte c, String nom) ;

  void gererCreationPersonnage(Contexte c, String nom, FabriquePersonnage fabrique);

  void gererInventaire(Contexte c);

  void gererMenu(Contexte c);

  void gererBoutique(Contexte c);

  void gererEquiper(Contexte c, String nom_objet);

  void gererDesequiper(Contexte c, String nom_objet);

  void gererConsommer(Contexte c, String nom_objet);

  void gererSortieDonjon(Contexte c);

  void gererAttaque(Contexte c, String nom);

  void gererPieceSuivante(Contexte c);

  void gererAcheter(Contexte c, String nom);

  void gererAmeliorer(Contexte c, String nom_objet);

  void gererEntrerMarchand(Contexte c);

  void gererSortieMarchand(Contexte c);

  void gererJeter(Contexte c, String nom_objet);

}
