package fr.univ.orleans.pnt.modele;

import fr.univ.orleans.pnt.modele.exceptions.*;

import java.time.LocalDateTime;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FacadeGestionPersonnes {

    private Map<String,Personne> personnes;

    public FacadeGestionPersonnes() {
        this.personnes = new HashMap<>();
    }


    /**
     * On suppose que toutes les valeurs entrées sont correctes
     * @param nom : non vide et non nulle
     * @param prenom non vide et non nulle
     * @param anneeNaissance : > 1900
     * @param email : email de la forme (a-z|A-Z|.|_|-)*@(a-z|A-Z|-)*.[fr|com]
     * @param numeroPortable : numero de la forme 0[6|7](0-9)*8
     * @return identifiant auto-généré
     */
    public String enregistrerPersonne(String nom, String prenom, String anneeNaissance, String email, String numeroPortable) throws DonneeIncorrecteException, EntierAttenduException, AnneeSuperieure1900AttendueException, AnneeSuperieureAnneeCouranteException, EmailIncorrectException, NumeroTelephonePortableIncorrectException {

        this.checkInfo(nom,prenom,anneeNaissance,email,numeroPortable);
        Integer anneeNaissanceInt = null;
        try {
            anneeNaissanceInt= Integer.valueOf(anneeNaissance);
        }
        catch (NumberFormatException e) {
            throw new EntierAttenduException();
        }

        if (anneeNaissanceInt < 1900){
            throw new AnneeSuperieure1900AttendueException();
        }

        if (anneeNaissanceInt > LocalDateTime.now().getYear()) {
            throw new AnneeSuperieureAnneeCouranteException();
        }

        String regexEmail = "^[a-zA-Z]+[.][a-zA-Z]+@([a-z|A-Z]+[.][a-z]{2}[a-z]?)$";

        Pattern pattern = Pattern.compile(regexEmail);

        Matcher matcher = pattern.matcher(email);

        if (!matcher.matches()) {
            throw new EmailIncorrectException();
        }


        String regexTelephone = "^0[6|7][0-9]{8}$";

        pattern = Pattern.compile(regexTelephone);

        matcher = pattern.matcher(numeroPortable);

        if (!matcher.matches()) {
            throw new NumeroTelephonePortableIncorrectException();
        }

        Personne personne = new Personne(nom,prenom,anneeNaissanceInt,email,numeroPortable);
        this.personnes.put(personne.getId(),personne);
        return personne.getId();
    }


    private void checkInfo(String... args) throws DonneeIncorrecteException {
        for (String x : args) {
            if (Objects.isNull(x) || x.isBlank()) {
                throw new DonneeIncorrecteException();
            }
        }
    }


    public Collection<Personne> getPersonnes(){
        return personnes.values();
    }



}
