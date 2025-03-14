package fr.univ.orleans.pnt.modele;

import java.util.UUID;

public class Personne {


    private String id;
    private String nom;
    private String prenom;
    private int anneeNaissance;
    private String email;
    private String numeroPortable;


    /**
     * Nous supposons que les informations sont correctes
     * @param nom
     * @param prenom
     * @param anneeNaissance
     * @param email
     * @param numeroPortable
     */
    public Personne(String nom, String prenom, int anneeNaissance, String email, String numeroPortable) {
        this.id = UUID.randomUUID().toString();
        this.nom = nom;
        this.prenom = prenom;
        this.anneeNaissance = anneeNaissance;
        this.email = email;
        this.numeroPortable = numeroPortable;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public int getAnneeNaissance() {
        return anneeNaissance;
    }

    public void setAnneeNaissance(int anneeNaissance) {
        this.anneeNaissance = anneeNaissance;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getNumeroPortable() {
        return numeroPortable;
    }

    public void setNumeroPortable(String numeroPortable) {
        this.numeroPortable = numeroPortable;
    }
}
