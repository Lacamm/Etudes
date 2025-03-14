
class Contexte implements Evenement{

    private Jeu monJeu;
    private EtatJeu etat_courant;

    public Contexte(Jeu monJeu)
    {
        this.monJeu = monJeu;
        this.etat_courant = new CreationPersonnage();
    }

    public Jeu getMonJeu(){ return this.monJeu;}

    public EtatJeu getEtat_courant(){return this.etat_courant;}

    public void set_etat_courant(EtatJeu etat){this.etat_courant = etat;}

    public void eventEntrerDonjon(String nom){
        etat_courant.gererEntreeDonjon(this,nom);
    }

    public void eventQuitterDonjon(){
        etat_courant.gererSortieDonjon(this);
    }

    public void eventCreationPersonnage(String nom, FabriquePersonnage fabrique){
        etat_courant.gererCreationPersonnage(this,nom,fabrique);
    }

    public void eventVoirInventaire(){
        etat_courant.gererInventaire(this);
    }

    public void eventVoirBoutique() {etat_courant.gererBoutique(this);}

    public void eventVoirMenu(){etat_courant.gererMenu(this);}

    public void eventEquiper(String nom_objet){ etat_courant.gererEquiper(this,nom_objet);}

    public void eventDesequiper(String nom_objet){etat_courant.gererDesequiper(this,nom_objet);}

    public void eventConsommer(String nom_objet){etat_courant.gererConsommer(this,nom_objet);}

    public void eventJeter(String nom_objet) {etat_courant.gererJeter(this,nom_objet);}

    public void eventAttaque(String nom) {etat_courant.gererAttaque(this,nom);}

    public void eventPieceSuivante() { etat_courant.gererPieceSuivante(this);}

    public void eventAcheter(String nom_objet) { etat_courant.gererAcheter(this,nom_objet);}

    public void eventAmeliorer(String nom_objet){ etat_courant.gererAmeliorer(this,nom_objet);}

    public void eventEntrerMarchand(){etat_courant.gererEntrerMarchand(this);}

    public void eventSortieMarchand(){etat_courant.gererSortieMarchand(this);}
}
