import java.rmi.RemoteException;
import java.util.*;


public class SondImpl implements Sondage {

    Hashtable<String, HashSet<Integer>> dicoDatesVotants;
    
    public SondImpl(){
        dicoDatesVotants = new Hashtable<String, HashSet<Integer>>();
    }

    @Override
    public void ajouterDate(String date) throws RemoteException{
        dicoDatesVotants.put(date, new HashSet<Integer>());
    }

    @Override
    public int nbVoixDate(String date) throws RemoteException {
        return dicoDatesVotants.get(date).size();
    }

    @Override
    public void ajouterVote(String date, int id) throws RemoteException {
        dicoDatesVotants.get(date).add(id);
    }

    @Override
    public String trouverDateChoisie() throws RemoteException {        
        int res = 0;
        String date = "";
        
        for (String k : dicoDatesVotants.keySet()){
            if(dicoDatesVotants.get(k).size() > res){
                res = dicoDatesVotants.get(k).size();
                date = k.toString();
            }
        }
        return date;
    }
}
