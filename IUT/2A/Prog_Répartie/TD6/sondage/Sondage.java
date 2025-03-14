import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Sondage extends Remote {

    void ajouterDate(String date) throws RemoteException;
    int nbVoixDate(String date) throws RemoteException;
    void ajouterVote(String date, int id) throws RemoteException;
    String trouverDateChoisie() throws RemoteException;
}