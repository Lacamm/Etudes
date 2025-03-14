package controleur.ordres;

public interface EcouteurOrdre {
    /**
     * Permet à un abonné de s'inscrire au près
     * d'un lanceur d'ordres
     * @param lanceur : le générateur concerné
     */
    void setAbonnement(LanceurOrdre lanceur);

    /**
     * Permet de décrire le traitement en fonction
     * de l'ordre reçu
     * @param ordre
     */
    void traiter(TypeOrdre ordre);
}
