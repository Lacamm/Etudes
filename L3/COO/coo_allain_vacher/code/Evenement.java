
interface Evenement {

  void eventEntrerDonjon(String nom) ;

  void eventQuitterDonjon();

  void eventCreationPersonnage(String nom,FabriquePersonnage fabrique) ;

  void eventVoirInventaire();

  void eventVoirBoutique();

  void eventVoirMenu();

  void eventDesequiper(String nom_objet);

  void eventConsommer(String nom_objet);

  void eventEquiper(String nom_objet);

  void eventJeter(String nom_objet);

  void eventAmeliorer(String nom_objet);

  void eventAttaque(String nom);

  void eventPieceSuivante();

  void eventAcheter(String nom_objet);

  void eventEntrerMarchand();

  void eventSortieMarchand();


}
