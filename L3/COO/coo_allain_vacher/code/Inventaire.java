import java.util.HashMap;
import java.util.Map;
import java.util.Set;


public class Inventaire {

    private Map<Objet,Integer> inventaire;
    private Map<Integer,Objet> equipement;
    private Personnage monPerso;

    public Inventaire(Personnage monPerso){
        this.inventaire = new HashMap<>();
        this.equipement = new HashMap<>();
        this.equipement.put(0,null);
        this.equipement.put(1,null);
        this.equipement.put(2,null);
        this.equipement.put(3,null);
        this.equipement.put(4,null);
        this.monPerso = monPerso;
    }

    public Inventaire InventaireDepart()
    {
        // Cette méthode permet de créer l'inventaire de départ du joueur
        Inventaire inventaireDepart = new Inventaire(this.monPerso);
        inventaireDepart.ajouterObjet(new Objet("Epee en pierre", Objet.TYPE.ARME,0,4,0,2,0,"Attaque +4"));
        Objet p = new Objet("Potion de vie", Objet.TYPE.CONSOMMABLE,0,0,0,2,5,"Rend 5 PV");
        inventaireDepart.ajouterObjet(p);
        inventaireDepart.ajouterObjet(p);
        inventaireDepart.ajouterObjet(new Objet("Potion de vie superieure",Objet.TYPE.CONSOMMABLE,0,0,0,2,10,"Rend 10 PV"));
        inventaireDepart.ajouterObjet(new Objet("Casque en cuir",Objet.TYPE.TETE,2,0,1,2,0,"PV +2 et Defense +1"));
        return inventaireDepart;
    }

    public Map<Objet, Integer> getInventaire() {
        return inventaire;
    }

    public boolean findObjet(String nom_objet)
    {
        // Cette méthode permet de savoir si un objet est présent ou non dans l'inventaire
        for(Map.Entry<Objet,Integer> entree : this.inventaire.entrySet())
        {
            if(entree.getKey().getNom().equals(nom_objet))
                return true;
        }
        return false;
    }

    public Objet getObjet(String nom_objet)
    {
        // Cette méthode retourne l'objet dans l'inventaire avec le nom en paramètre
        if(findObjet(nom_objet))
        {
            for(Map.Entry<Objet,Integer> entree : this.inventaire.entrySet())
            {
                if(entree.getKey().getNom().equals(nom_objet))
                    return entree.getKey();
            }
        }
        return null;
    }

    public boolean findEquipement(String nom_equipement)
    {
        // Cette méthode permet de savoir si un objet est présent ou non dans les équipements
        for(Map.Entry<Integer,Objet> entree : this.equipement.entrySet())
        {
            if(entree.getValue() != null)
            {
                if(entree.getValue().getNom().equals(nom_equipement))
                    return true;
            }
        }
        return false;
    }

    public Objet getEquipement(String nom_equipement){
        // Cette méthode retourne l'objet dans les équipements avec le nom en paramètre
        if(findEquipement(nom_equipement))
        {
            for(Map.Entry<Integer,Objet> entree : this.equipement.entrySet())
            {
                if(entree.getValue() != null)
                {
                    if(entree.getValue().getNom().equals(nom_equipement))
                        return entree.getValue();
                }
            }
        }
        return null;
    }

    public void jeterObjet(String nom_objet){
        // Cette méthode permet de jeter un objet de l'inventaire
        Objet objet = this.getObjet(nom_objet);
        if(objet != null) {
            if (this.inventaire.get(objet) != 1)
                this.inventaire.put(objet, this.inventaire.get(objet) - 1);
            else
                this.inventaire.remove(objet);
            System.out.println(this.monPerso.getNom() + " jette l'objet " + nom_objet);
        }
        else
            System.out.println("L'objet que vous voulez jeter n'est pas dans votre inventaire");
    }

    public void ajouterObjet(Objet objet)
    {
        // Cette méthode permet d'ajouter un objet à l'inventaire
        boolean test = false;
        for(Map.Entry<Objet,Integer> entree : this.inventaire.entrySet())
        {
            if(entree.getKey().getNom().equals(objet.getNom()))
            {
                this.inventaire.put(objet,this.inventaire.get(objet) + 1);
                test = true;
            }
        }
        if(!test)
            this.inventaire.put(objet,1);
    }

    public void consommeObjet(String nom_objet){
        // Cette méthode permet de consommer un objet
        Objet objet = this.getObjet(nom_objet);
        if(objet != null) {
            if (objet.getType() == Objet.TYPE.CONSOMMABLE) {
                if (this.monPerso.getVie() + objet.getPvRendu() > this.monPerso.getVieMax())
                    this.monPerso.setVie(this.monPerso.getVieMax());
                else
                    this.monPerso.setVie(this.monPerso.getVie() + objet.getPvRendu());
                if(this.inventaire.get(objet) == 1)
                    this.inventaire.remove(objet);
                else
                    this.inventaire.put(objet,this.inventaire.get(objet) - 1);
                System.out.println(this.monPerso.getNom() + " utilise " + nom_objet + ", sa vie est maintenant de : " + this.monPerso.getVie() + "/" + this.monPerso.getVieMax());
            }
        }
        else
            System.out.println("L'objet " + nom_objet + " ne peut pas être consommé");
    }

    public void desequiper(String nom_objet){
        // Cette méthode permet de désequiper un objet
        Objet objet = this.getEquipement(nom_objet);
        if(objet == null)
            System.out.println("L'objet demandé n'est pas équipé.");
        else{
            if(objet.getType() == Objet.TYPE.TETE){
                if(this.equipement.get(0) != null){
                    if(this.inventaire.containsKey(this.equipement.get(0)))
                        this.inventaire.put(this.equipement.get(0), this.inventaire.get(this.equipement.get(0)) + 1);
                    else
                        this.inventaire.put(this.equipement.get(0),1);
                    this.equipement.put(0,null);
                }
                else
                    System.out.println("Vous n'avez rien d'équipé ici.");
            }
            if(objet.getType() == Objet.TYPE.BUSTE){
                if(this.equipement.get(1) != null){
                    if(this.inventaire.containsKey(this.equipement.get(1)))
                        this.inventaire.put(this.equipement.get(1), this.inventaire.get(this.equipement.get(1)) + 1);
                    else
                        this.inventaire.put(this.equipement.get(1),1);
                    this.equipement.put(1,null);
                }
                else
                    System.out.println("Vous n'avez rien d'équipé ici.");
            }
            if(objet.getType() == Objet.TYPE.JAMBES){
                if(this.equipement.get(2) != null){
                    if(this.inventaire.containsKey(this.equipement.get(2)))
                        this.inventaire.put(this.equipement.get(2), this.inventaire.get(this.equipement.get(2)) + 1);
                    else
                        this.inventaire.put(this.equipement.get(2),1);
                    this.equipement.put(2,null);
                }
                else
                    System.out.println("Vous n'avez rien d'équipé ici.");
            }
            if(objet.getType() == Objet.TYPE.PIEDS){
                if(this.equipement.get(3) != null){
                    if(this.inventaire.containsKey(this.equipement.get(3)))
                        this.inventaire.put(this.equipement.get(3), this.inventaire.get(this.equipement.get(3)) + 1);
                    else
                        this.inventaire.put(this.equipement.get(3),1);
                    this.equipement.put(3,null);
                }
                else
                    System.out.println("Vous n'avez rien d'équipé ici.");
            }
            if(objet.getType() == Objet.TYPE.ARME){
                if(this.equipement.get(4) != null){
                    if(this.inventaire.containsKey(this.equipement.get(0)))
                        this.inventaire.put(this.equipement.get(4), this.inventaire.get(this.equipement.get(4)) + 1);
                    else
                        this.inventaire.put(this.equipement.get(4),1);
                    this.equipement.put(4,null);
                }
                else
                    System.out.println("Vous n'avez rien d'équipé ici.");
            }
            System.out.println(this.monPerso.getNom() + " se désequipe de l'objet " + nom_objet + ".");
            monPerso.downgradeStats(objet);
        }
    }

    public void equiper(String nom_objet){
        // Cette méthode permet d'équiper un objet
        Objet objet = this.getObjet(nom_objet);
        if(objet != null) {
            if (objet.getType() == Objet.TYPE.TETE) {
                if (this.equipement.containsKey(0)) {
                    if (this.equipement.get(0) != null) {
                        Objet equipement = this.equipement.get(0);
                        if (findObjet(equipement.getNom())) {
                            this.inventaire.put(equipement, this.inventaire.get(equipement) + 1);
                        } else
                            this.inventaire.put(equipement, 1);
                        this.monPerso.downgradeStats(equipement);
                    }
                }
                this.equipement.put(0, objet);
            }
            if (objet.getType() == Objet.TYPE.BUSTE) {
                if (this.equipement.containsKey(1)) {
                    if (this.equipement.get(1) != null) {
                        Objet equipement = this.equipement.get(1);
                        if (findObjet(equipement.getNom()))
                            this.inventaire.put(equipement, this.inventaire.get(equipement) + 1);
                        else
                            this.inventaire.put(equipement, 1);
                        this.monPerso.downgradeStats(equipement);
                    }
                }
                this.equipement.put(1, objet);
            }
            if (objet.getType() == Objet.TYPE.JAMBES) {
                if (this.equipement.containsKey(2)) {
                    if (this.equipement.get(2) != null) {
                        Objet equipement = this.equipement.get(2);
                        if (findObjet(equipement.getNom()))
                            this.inventaire.put(equipement, this.inventaire.get(equipement) + 1);
                        else
                            this.inventaire.put(equipement, 1);
                        this.monPerso.downgradeStats(equipement);
                    }
                }
                this.equipement.put(2, objet);
            }
            if (objet.getType() == Objet.TYPE.PIEDS) {
                if (this.equipement.containsKey(3)) {
                    if (this.equipement.get(3) != null) {
                        Objet equipement = this.equipement.get(3);
                        if (findObjet(equipement.getNom()))
                            this.inventaire.put(equipement, this.inventaire.get(equipement) + 1);
                        else
                            this.inventaire.put(equipement, 1);
                        this.monPerso.downgradeStats(equipement);
                    }
                }
                this.equipement.put(3, objet);
            }
            if (objet.getType() == Objet.TYPE.ARME) {
                if (this.equipement.containsKey(4)) {
                    if (this.equipement.get(4) != null) {
                        Objet equipement = this.equipement.get(4);
                        if (findObjet(equipement.getNom()))
                            this.inventaire.put(equipement, this.inventaire.get(equipement) + 1);
                        else
                            this.inventaire.put(equipement, 1);
                        this.monPerso.downgradeStats(equipement);
                    }
                }
                this.equipement.put(4, objet);
            }
            if (objet.getType() != Objet.TYPE.CONSOMMABLE) {

                if (this.inventaire.get(objet) == 1)
                    this.inventaire.remove(objet);
                else
                    this.inventaire.put(objet, this.inventaire.get(objet) - 1);
                System.out.println(this.monPerso.getNom() + " équipe l'objet " + nom_objet);
                monPerso.upgradeStats(objet);
            }
            else
                System.out.println("Vous essayer d'équiper un consommable, ce n'est pas possible.");
        }
        else
            System.out.println("L'objet " + nom_objet + " n'est pas dans l'inventaire.");

    }

    public void afficherInventaire(){
        // Cette méthode permet d'afficher l'inventaire
        System.out.println("=========== Inventaire de " + this.monPerso.getNom() + " ===========");
        System.out.println("Argent disponible : " + this.monPerso.getArgent() + " $");
        System.out.println("Objets équipés : \n");
        this.afficherEquipement();
        System.out.println(" \nObjets présents dans l'inventaire : \n");
        for(Map.Entry<Objet,Integer> entree : this.inventaire.entrySet())
        {
            if(entree.getKey().isAmeliore())
            {
                System.out.println( entree.getKey().getNom() + " : " + entree.getValue() + " (Amelioré) => " + entree.getKey().getEffet());
            }
            else{
                System.out.println( entree.getKey().getNom() + " : " + entree.getValue() + " => " + entree.getKey().getEffet());
            }
        }
        System.out.println("=========================================" + "\n");
    }

    public void afficherEquipement(){
        // Cette méthode permet d'afficher l'équipement
        for(int i = 0; i < this.equipement.size(); ++i) {
            if (i == 0) {
                if (this.equipement.get(0) == null)
                    System.out.println("Casque : Vide");
                else if (this.equipement.get(0).isAmeliore()) {
                    System.out.println("Casque : " + this.equipement.get(0).getNom() + " (Amelioré) => " + this.equipement.get(0).getEffet());
                } else {
                    System.out.println("Casque : " + this.equipement.get(0).getNom() + " => " + this.equipement.get(0).getEffet());
                }
            }
            if(i == 1) {
                if (this.equipement.get(1) == null)
                    System.out.println("Plastron : Vide");
                else if (this.equipement.get(1).isAmeliore()) {
                    System.out.println("Plastron: " + this.equipement.get(1).getNom() + " (Amelioré) => " + this.equipement.get(1).getEffet());
                } else {
                    System.out.println("Plastron : " + this.equipement.get(1).getNom() + " => " + this.equipement.get(1).getEffet());
                }
            }
            if(i == 2) {
                if (this.equipement.get(2) == null)
                    System.out.println("Jambières : Vide");
                else if (this.equipement.get(2).isAmeliore()) {
                    System.out.println("Jambières : " + this.equipement.get(2).getNom() + " (Amelioré) => " + this.equipement.get(2).getEffet());
                } else {
                    System.out.println("Jambières : " + this.equipement.get(2).getNom() + " => " + this.equipement.get(2).getEffet());
                }
            }
            if(i == 3) {
                if (this.equipement.get(3) == null)
                    System.out.println("Pieds : Vide");
                else if (this.equipement.get(3).isAmeliore()) {
                    System.out.println("Pieds : " + this.equipement.get(3).getNom() + " (Amelioré) => " + this.equipement.get(3).getEffet());
                } else {
                    System.out.println("Pieds : " + this.equipement.get(3).getNom() + " => " + this.equipement.get(3).getEffet());
                }
            }
            if(i == 4)
            {
                if(this.equipement.get(4) == null)
                    System.out.println("Arme : Vide");
                else if (this.equipement.get(4).isAmeliore()) {
                    System.out.println("Arme : " + this.equipement.get(4).getNom() + " (Amelioré) => " + this.equipement.get(4).getEffet());
                } else {
                    System.out.println("Arme : " + this.equipement.get(4).getNom() + " => " + this.equipement.get(4).getEffet());
                }
            }

        }
    }
    public void desequiperA(Objet objet) {
        // Cette méthode permet de désequiper un objet

        if (objet.getType() == Objet.TYPE.TETE)
            this.equipement.put(0,null);
        if (objet.getType() == Objet.TYPE.BUSTE)
            this.equipement.put(1,null);
        if (objet.getType() == Objet.TYPE.JAMBES)
            this.equipement.put(2,null);
        if (objet.getType() == Objet.TYPE.PIEDS)
            this.equipement.put(3,null);
        if (objet.getType() == Objet.TYPE.ARME)
            this.equipement.put(4,null);
        monPerso.downgradeStats(objet);
    }

    public void equiperA(Objet objet) {
        // Cette méthode permet d'équiper un objet
        if (objet.getType() == Objet.TYPE.TETE)
            this.equipement.put(0, objet);
        if (objet.getType() == Objet.TYPE.BUSTE)
            this.equipement.put(1, objet);
        if (objet.getType() == Objet.TYPE.JAMBES)
            this.equipement.put(2, objet);
        if (objet.getType() == Objet.TYPE.PIEDS)
            this.equipement.put(3, objet);
        if (objet.getType() == Objet.TYPE.ARME)
            this.equipement.put(4, objet);
        monPerso.upgradeStats(objet);

    }
}
