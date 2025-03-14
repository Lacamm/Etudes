import java.util.concurrent.locks.*;
import java.util.*;

class Messages{

    List<String> messages;

    public Messages(){
	messages= new ArrayList<String>();
    }
    
    public String lireLePlusRecent(){
      Lock lk = new ReentrantLock();
      lk.lock();
      String dernier="";
      if (messages!=null)
	 dernier =messages.get(0);
      lk.unlock();
      return dernier;
    }

    public void ajouterMessage(String message){
	messages.add(message);
    }

    public static void main(String args[]){
      Messages messages = new Messages();
      T1 t1 = new T1(messages); t1.start();
      T1 t2 = new T1(messages); t2.start();
    }
}

class T1 extends Thread{
    Messages messages;
    T1(Messages messages){
      this.messages = messages;
    }

    public void run(){
      Lock lk = new ReentrantLock();
      lk.lock();
        messages.ajouterMessage("Bonjour");
      lk.unlock();
      System.out.println(messages.lireLePlusRecent());
    }
    
}

