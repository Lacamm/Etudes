package com.example.jamian.first;

import android.util.Log;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

/**
 * Created by jamian on 21/11/16.
 */
public class ListeMessages {

    public static final String TAG = "WSLastMessages";

    ArrayList listeMessage = new ArrayList<Message>();

    public ListeMessages() throws IOException {
        //ajouteMessage(1,Calendar.getInstance().getTime(),"Riri","Bonjour Bonjour");
        //ajouteMessage(2,Calendar.getInstance().getTime(),"Fifi","Et un autre message");
        //ajouteMessage(3,Calendar.getInstance().getTime(),"Loulou","On va faire un message un peu plus long, pour voir comment ça passe sur tous les affichages. Hopla ! Et même encore un peu plus long histoire de dire. Après tout, normalement on a tout un écran pour l'afficher, donc on est bien large...");

    }

    public void ajouteMessage(int id, Date date, String author, String contenu) {
        Message message = new Message(id, author, contenu, date);
        listeMessage.add(message);
    }

    public Message get(int i) { //from index
        return (Message) listeMessage.get(i);
    }

    public boolean deleteMessageFromIndex(int i) {
        return listeMessage.remove(listeMessage.get(i));
    }

    public int deleteMessageFromId(int id) {
        for (int j=0; j<listeMessage.size(); j++){
            Message message = (Message) listeMessage.get(j);
            if (message.getId() == id){
                listeMessage.remove(listeMessage.get(j));
                return j;
            }
        }
        return -1;
    }

    public int size() {
        return listeMessage.size();
    }

    // WebServices
    public ArrayList<Message> call() {
        try {
            URL url = new URL("http://51.68.124.144/ws_chat/last_msg.php");
            URLConnection cnx = url.openConnection();
            InputStream in = cnx.getInputStream();

            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document xml = db.parse(in);

            NodeList nl = xml.getElementsByTagName("STATUS");
            Node nodeStatus = nl.item(0);
            String status = nodeStatus.getTextContent();
            Log.d(TAG, "Thread last msg : status " + status);
            if (!status.startsWith("OK"))
                return null;
            nl = xml.getElementsByTagName("CONTENT");
            Node nodeContent = nl.item(0);
            NodeList messagesXML = nodeContent.getChildNodes();

            ArrayList<Message> aAjouter = new ArrayList<Message>();
            for (int i = 0; i < messagesXML.getLength(); i++) {
                Node message = messagesXML.item(i);
                aAjouter.add(parseMessage(message));
            }
            return aAjouter;
        }
        catch (Exception e){
            e.printStackTrace();
            return null;
        }
    }

    private Message parseMessage(Node msgNode) {
        int id = -1;
        String auteur = null;
        String contenu = null;
        String stringDate = null;
        NodeList messageFields = msgNode.getChildNodes();
        for (int j = 0; j < messageFields.getLength(); j++) {
            Node field = messageFields.item(j);
            if (field.getNodeName().equalsIgnoreCase("ID"))
                id = Integer.parseInt(field.getTextContent());
            else if (field.getNodeName().equalsIgnoreCase("DATESENT"))
                stringDate = field.getTextContent();
            else if (field.getNodeName().equalsIgnoreCase("AUTHOR"))
                auteur = field.getTextContent();
            else if (field.getNodeName().equalsIgnoreCase("MSG"))
                contenu = field.getTextContent();
        }
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        assert stringDate != null;
        Date date = null;
        try {
            date = formatter.parse(stringDate);
        } catch (ParseException e) {
            e.printStackTrace();
            return null;
        }
        assert auteur != null;
        assert contenu != null;
        assert date != null;
        return new Message(id, auteur, contenu, date);
    }
}
