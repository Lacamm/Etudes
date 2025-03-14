import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.Random;


class Jeu implements Evenement{

    private Personnage personnage_courant;
    private Contexte monContexte;
    private Donjon donjon_courant;
    private Piece piece_courante;
    private List<Donjon> listeDonjons;
    private int nombre_piece_courante;
    private Marchand marchand;

    public Jeu()
    {
        this.listeDonjons = new ArrayList<>();
    }

    public Personnage getPersonnage(){
        return this.personnage_courant;
    }

    public int getNombre_piece_courante() {
        return nombre_piece_courante;
    }
    public Donjon getDonjon(String nom){
        for(Donjon donjon : this.listeDonjons)
        {
            if(donjon.getNom().equals(nom))
                return donjon;
        }
        return null;
    }

    public boolean findDonjon(String nom){
        for(Donjon donjon : this.listeDonjons)
        {
            if(donjon.getNom().equals(nom))
                return true;
        }
        return false;
    }

    public void setMonContexte(Contexte monContexte) {
        this.monContexte = monContexte;
    }

    public EtatJeu getEtatCourant(){ return monContexte.getEtat_courant();}

    public Donjon getDonjon_courant() {
        return this.donjon_courant;
    }

    public Piece getPiece_courante() {
        return this.piece_courante;
    }

    public Personnage getPersonnage_courant() {
        return personnage_courant;
    }

    public void add_donjon(Donjon donjon){ this.listeDonjons.add(donjon);}


    public void afficherMenu()
    {
        System.out.println("############## Menu ##############");
        System.out.println("Liste des donjons disponibles : ");
        for(Donjon donjon : this.listeDonjons) {
                if (donjon.isReussi())
                    System.out.println(donjon.getNom() + ": Réussi");
                else
                    System.out.println(donjon.getNom() + ": Non réussi");
        }
        System.out.println("###################################\n");

    }

    public void creer_Personnage(String nom, FabriquePersonnage fabrique)
    {
        // Cette méthode permet de créer un personnage avec la fabrique passée en paramètre
        this.personnage_courant = fabrique.creerPersonnage(nom);
        System.out.println("Le personnage " + nom + " de la classe " + this.personnage_courant.getClasse() + " a été crée.");
    }

    public void entrerDonjon(String nom){
        // Cette méthode permet d'entrer dans un donjon
        if(this.findDonjon(nom)) {
            this.donjon_courant = this.getDonjon(nom);
            System.out.println(this.getPersonnage_courant().getNom() + " décide d'aller dans le donjon " + nom + ".");
            this.piece_courante = this.donjon_courant.get_piece(0);
            this.nombre_piece_courante = 0;
            System.out.println("############## " + this.personnage_courant.getNom() + " entre dans un donjon ##############");
            if(this.piece_courante.getNbEnnemis() == 0)
                System.out.println("Il n'y a plus aucun ennemi ici");
            else
                this.piece_courante.afficher_ennemis();
        }
        else
            System.out.println("Le donjon " + nom + " n'existe pas.");
    }

    public void attaquer(String nom_adversaire)
    {
        // Cette méthode permet de faire attaquer tout les PNJ présents dans une pièce (le personnage comme les montres)
        ArrayList<PNJ> morts = new ArrayList<>();
        this.personnage_courant.attaquer(this.piece_courante.getEnnemis(nom_adversaire));
        boolean estMort = false;
        for(PNJ adversaires : this.piece_courante.getListeEnnemis())
        {
            if(adversaires.getVie() <= 0)
                morts.add(adversaires);
            else {
                if(this.personnage_courant.getVie() <= 0)
                    estMort = true;
                if (!estMort) {
                    adversaires.attaquer(this.personnage_courant);
                }
            }
        }
        // Verification des monstres qui ont été tué ( realisé ici car exception sinon)
        if(!morts.isEmpty())
        {
            for(PNJ mort : morts)
            {
                this.piece_courante.delEnnemis(mort);
                this.piece_courante.getListeVaincus().add(mort);
            }
        }

        // Affichage des PV de tout le monde
        if(this.personnage_courant.getVie() >= 0)
        {
            System.out.println("============= Fin de tour ==========");
            System.out.println("PV de " + this.personnage_courant.getNom() + " : " + this.personnage_courant.getVie() + "/" + this.personnage_courant.getVieMax());
            for(PNJ adversaires : this.piece_courante.getListeEnnemis())
            {
                System.out.println("PV de " + adversaires.getNom() + " le " + adversaires.getClasse() + " : " + adversaires.getVie() + "/" + adversaires.getVieMax());
            }
            System.out.println("===================================");
        }
    }

    public void pieceSuivante()
    {
        // Cette méthode permet de changer de pièce
        this.piece_courante = this.donjon_courant.get_piece(this.nombre_piece_courante + 1);
        this.nombre_piece_courante+= 1;
        System.out.println(this.personnage_courant.getNom() + " change de pièce.");
        if(this.piece_courante.getNbEnnemis() == 0)
            System.out.println("Il n'y a plus aucun ennemi ici");
        else
            this.piece_courante.afficher_ennemis();
    }

    public void sortieDonjon()
    {
        // Cette méthode permet de sortir du donjon dans le cas ou le donjon est fini
        if(!this.donjon_courant.isReussi()) {
            System.out.println("Le donjon est terminée, les récompenses de ce donjon vont être ajouté à votre inventaire.");
            System.out.println("Voici la liste des récompenses : ");
            System.out.println("    Argent => 20 $");
            this.donjon_courant.setReussi(true);
            this.personnage_courant.setArgent(this.personnage_courant.getArgent() + 20);
            for (Objet recompenses : this.donjon_courant.getRecompenses()) {
                System.out.println("    " + recompenses.getNom() + " => " + recompenses.getEffet());
                this.personnage_courant.getMonInventaire().ajouterObjet(recompenses);
            }
            System.out.println("\n############## " + this.personnage_courant.getNom() + " sort du donjon ##############\n");
        }
        else{
            System.out.println("Le donjon est terminée, cependant, vous l'aviez déja fini, vous ne recevrez donc aucune récompense");
            System.out.println("\n############## " + this.personnage_courant.getNom() + " sort du donjon ##############\n");
        }
    }

    public void fuirDonjon(){
        // Cette méthode permet de sortir du donjon avant de le finir
        this.donjon_courant.save();
        System.out.println(this.personnage_courant.getNom() + " décide de fuir.");
        System.out.println("\n############## " + this.personnage_courant.getNom() + " sort du donjon " + this.donjon_courant.getNom() + " ##############\n");
    }

    public void mortPerso() {
        // On recupere le nom de tous les items dans l'inventaire
        System.out.println("✞ Vous êtes mort ✞");
        ArrayList<String> nom_items = new ArrayList<>();
        for (Map.Entry<Objet, Integer> entree : this.personnage_courant.getMonInventaire().getInventaire().entrySet()) {
            if (entree.getValue() == 1)
                nom_items.add(entree.getKey().getNom());
            else {
                for (int i = 0; i < entree.getValue(); i++) {
                    nom_items.add(entree.getKey().getNom());
                }
            }
        }
        // On supprime ensuite 1/3 des items présents dans l'inventaire
        int cpt = (nom_items.size() / 3);
        if(cpt == 0) // Il se peut qu'avec la convertion, cpt soit egal à 0
            cpt = 1;
        int alea = 0;
        System.out.println("Vous perdez la moitié de votre argent ainsi que ces items :");
        for (int y = 0; y < cpt; y++) {
            Random random = new Random();
            alea = random.nextInt(nom_items.size());
            System.out.println("    " + nom_items.get(alea));
            Objet objet = this.personnage_courant.getMonInventaire().getObjet(nom_items.get(alea));
            if(this.personnage_courant.getMonInventaire().getInventaire().get(objet) == 1)
                this.personnage_courant.getMonInventaire().getInventaire().remove(objet);
            else
                this.personnage_courant.getMonInventaire().getInventaire().put(objet,this.personnage_courant.getMonInventaire().getInventaire().get(objet) - 1);
            nom_items.remove(alea);
        }
        this.personnage_courant.setVie(1);
        this.personnage_courant.setArgent(this.personnage_courant.getArgent() / 2);
        this.donjon_courant.save();
    }

    public void ameliorer(String nom_objet)
    {
        Objet inventaire = this.getPersonnage().getMonInventaire().getObjet(nom_objet);
        Objet equipement = this.getPersonnage().getMonInventaire().getEquipement(nom_objet);
        if(inventaire != null) {
            if (inventaire.getType() != Objet.TYPE.CONSOMMABLE) {
                if (!inventaire.isAmeliore()) {
                    if (this.personnage_courant.getArgent() >= 5) {
                        Amelioration a = new Forger(inventaire);
                        this.personnage_courant.setArgent(this.personnage_courant.getArgent() - 5);
                        System.out.println(nom_objet + " a été amélioré");
                        System.out.println("Il reste à "+this.personnage_courant.getNom() + " " + this.personnage_courant.getArgent() + " $");
                    } else {
                        System.out.println("Vous n'avez pas assez d'argent pour améliorer votre " + nom_objet);
                    }
                }
                else{
                    System.out.println("Votre objet est déja amélioré");
                }
            }
            else
            {
                System.out.println("Vous ne pouvez pas améliorer un consommable");
            }
        }
        else if(equipement != null) {
            if (equipement.getType() != Objet.TYPE.CONSOMMABLE) {
                if (!equipement.isAmeliore()) {
                    if (this.personnage_courant.getArgent() >= 5) {
                        this.personnage_courant.desequiperObjetA(equipement);
                        Amelioration ameliore = new Forger(equipement);
                        this.personnage_courant.equiperObjetA(equipement);
                        this.personnage_courant.setArgent(this.personnage_courant.getArgent() - 5);
                        System.out.println(nom_objet + " a été amélioré");
                        System.out.println("Il reste à "+this.personnage_courant.getNom() + " " + this.personnage_courant.getArgent() + " $");
                    } else {
                        System.out.println("Vous n'avez pas assez d'argent pour améliorer votre " + nom_objet);
                    }
                }
                else{
                    System.out.println("Votre objet est déja amélioré");
                }
            }
            else
            {
                System.out.println("Vous ne pouvez pas améliorer un consommable");
            }
        }
        else{
            System.out.println("Vous ne possedez pas l'objet " + nom_objet);
        }

    }

    public void equiperObjet(String nom_objet)
    {
        this.personnage_courant.equiperObjet(nom_objet);
    }

    public void desequiperObjet(String nom_objet)
    {
        this.personnage_courant.desequiperObjet(nom_objet);
    }

    public void consommerObjet(String nom_objet)
    {
        this.personnage_courant.consommerObjet(nom_objet);
    }

    public void jeterObjet(String nom_objet) {this.personnage_courant.jeterObjet(nom_objet);}

    public void addMarchand(Marchand marchand)
    {
        this.marchand = marchand;
    }

    public void afficherBoutique()
    {
        this.marchand.afficherBoutique();
    }

    public void afficherStocks()
    {
        this.marchand.afficherStocks();
    }

    public void acheter(String nom_objet)
    {
        this.marchand.acheter(this.personnage_courant,nom_objet);
    }


    public void eventEntrerDonjon(String nom){
       monContexte.eventEntrerDonjon(nom);
    }

    public void eventQuitterDonjon(){
        monContexte.eventQuitterDonjon();
    }

    public void eventCreationPersonnage(String nom, FabriquePersonnage fabrique){
        monContexte.eventCreationPersonnage(nom,fabrique);
    }

    public void eventVoirInventaire(){
        monContexte.eventVoirInventaire();
    }

    public void eventVoirBoutique() {monContexte.eventVoirBoutique();}

    public void eventEquiper(String nom_objet) {monContexte.eventEquiper(nom_objet);}

    public void eventDesequiper(String nom_objet){monContexte.eventDesequiper(nom_objet);}

    public void eventConsommer(String nom_objet){monContexte.eventConsommer(nom_objet);}

    public void eventJeter(String nom_objet) {monContexte.eventJeter(nom_objet);}

    public void eventAttaque(String nom) {monContexte.eventAttaque(nom);}

    public void eventPieceSuivante(){ monContexte.eventPieceSuivante();}

    public void eventAcheter(String nom_objet) { monContexte.eventAcheter(nom_objet);}

    public void eventAmeliorer(String nom_objet){ monContexte.eventAmeliorer(nom_objet);}

    public void eventEntrerMarchand(){monContexte.eventEntrerMarchand();}

    public void eventSortieMarchand(){monContexte.eventSortieMarchand();}

    public void eventVoirMenu(){monContexte.eventVoirMenu();}

}
