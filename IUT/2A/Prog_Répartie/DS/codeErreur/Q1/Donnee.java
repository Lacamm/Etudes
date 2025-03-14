import java.util.concurrent.locks.*;

/**
Classe utile dans le cadre d'un Producteur/consommateur
 **/
class Donnee{


    Object valeur;
    Lock verrou;
    Condition attente;

    
    public synchronized void ajout(Object nouvelleValeur) throws Exception{
	verrou.lock();
	if (valeur!=null)
	    attente.wait();
	
	valeur=nouvelleValeur;
	verrou.unlock();
    }

    public synchronized  Object recuperer() throws Exception {
	verrou.lock();
	if (valeur==null)
	    attente.wait();

	    Object retour = valeur;
	    valeur = null;
	    return retour;
    }
    

    
}

