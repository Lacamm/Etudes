import java.io.Console;
import java.io.FileReader;
import java.io.Writer;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;
import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;

public class App {
    public static void main(String[] args)
	throws Exception	       
    {
	System.out.println("Bienvenue dans Top Questionnaire 2000");

	JSONParser parser = new JSONParser();
	Console cons = System.console();
	
	FileReader f = new FileReader(args[0]);
	JSONArray obj = (JSONArray) parser.parse(f);

	Questionnaire q = Questionnaire.fromJson(obj);
	q.pose(cons);
    }
}

interface Question {
    void pose(Console c);
}

class QuestionOuverte implements Question {

    String contenu;
    
    public QuestionOuverte(String contenu) {
	this.contenu = contenu;
    }
    
    public void pose(Console console) {
	System.out.println(contenu);
	console.readLine();
    }

    public static QuestionOuverte fromJson(JSONObject json) {
	QuestionOuverte q = new QuestionOuverte((String) json.get("contenu"));
	return q;
    }
}

class QuestionChoixMultiples implements Question {
    
    String question;
    List<String> reponses;

    public QuestionChoixMultiples(String question, List<String> reponses) {
	this.question = question;
	this.reponses = reponses;
    }

    public int pose_garde_reponse(Console console) {
	int n = this.reponses.size();
	int k = -1;
	
	while (k < 0 || k >= n) {
	    System.out.println(this.question);
	    for ( int i = 0; i < n; i++) {
		System.out.print(i);
		System.out.print(": ");
		System.out.println(reponses.get(i));
	    }

	    String s_k = console.readLine();
	    try {
		k = Integer.parseInt(s_k);
	    } catch (NumberFormatException e) {
	    };
	}

	return k;
    }
    
    public void pose(Console console) {
	this.pose_garde_reponse(console);
    }

    public static QuestionChoixMultiples fromJson(JSONObject json) throws Exception {
	
	String question = (String) json.get("question");
	JSONArray reponses_json = (JSONArray) json.get("reponses");

	ArrayList<String> reponses = new ArrayList();
	for (Object r: reponses_json) {
	   reponses.add((String) r);
	}
	
	QuestionChoixMultiples q = new QuestionChoixMultiples(question, reponses);
	return q;
    }
}

class QuestionCMApprofondie extends QuestionChoixMultiples {
    
    List<Question> sous_questions;
    
    public QuestionCMApprofondie(String question, List<String> reponses, List<Question> sous_questions) {
	super(question, reponses);
	this.sous_questions = sous_questions;
    }

    public void pose(Console console) {
	System.out.println("Argh, la méthode pose n'a pas été implémentée pour la classe QuestionCMApprofondie");
	System.out.println("Ce questionnaire ne peut donc être lu avant d'avoir fait la question 3");
    }

    public static QuestionCMApprofondie fromJson(JSONObject json) throws Exception
    {
	
	String question = (String) json.get("question");
	JSONArray reponses_json = (JSONArray) json.get("reponses");
	JSONArray sous_questions_json = (JSONArray) json.get("sous-questions");

	ArrayList<String> reponses = new ArrayList();
	for (Object r: reponses_json) {
	    reponses.add((String) r);
	}

	ArrayList<Question> sous_questions = new ArrayList();
	for (Object q_obj: sous_questions_json) {
	    JSONObject q_json = (JSONObject) q_obj;
	    String type = (String) q_json.get("type");

	    Question q;
	    switch(type) {
	    case "ouverte":
		q = QuestionOuverte.fromJson(q_json);
		break;
	    case "choix multiples":
		q = QuestionChoixMultiples.fromJson(q_json);
		break;
	    case "approfondie":
		q = QuestionCMApprofondie.fromJson(q_json);
		break;
	    default:
		throw new QuestionnaireParseException();
	    }
	    sous_questions.add(q);
	}
	
	QuestionCMApprofondie q = new QuestionCMApprofondie(question, reponses, sous_questions);
	return q;
    }

}

class QuestionnaireParseException extends Exception {

}

class Questionnaire {

    
    List<Question> questions;

    public Questionnaire(List<Question> questions) {
	this.questions = questions;
    }

    public void pose(Console console) {
	for(Question q: this.questions) {
	    q.pose(console);
	}
    }

    
    // public void pose_et_sauve(Console console, Writer out) throws Exception {
    // 	for(Question q: this.questions) {
    // 	    q.pose_et_sauve(console, out);
    // 	}
    // }


    public static Questionnaire fromJson(JSONArray json) throws Exception {
	ArrayList<Question> questions = new ArrayList();
	for (Object o: json) {
	    JSONObject q_json = (JSONObject) o;
	    String type = (String) q_json.get("type");

	    Question q;
	    switch(type) {
	    case "ouverte":
		q = QuestionOuverte.fromJson(q_json);
		break;
	    case "choix multiples":
		q = QuestionChoixMultiples.fromJson(q_json);
		break;
	    case "approfondie":
		q = QuestionCMApprofondie.fromJson(q_json);
		break;
	    default:
		throw new QuestionnaireParseException();
	    }
	    questions.add(q);
	}
	return new Questionnaire(questions);
    }
}
