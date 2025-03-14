package controleur;

import facade.FacadeParis;
import facade.FacadeParisStaticImpl;
import facade.exceptions.InformationsSaisiesIncoherentesException;
import facade.exceptions.OperationNonAuthoriseeException;
import facade.exceptions.UtilisateurDejaConnecteException;
import modele.Match;
import modele.Pari;
import modele.Utilisateur;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Collection;


@WebServlet(name="connexion", urlPatterns ="/pel/*")
public class Controleur extends HttpServlet {

//    @Override
//    public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
//        req.getServletContext()
//                .getRequestDispatcher("/jsp/Connexion.jsp")
//                .forward(req,res);
//    }

    public static final String CONNEXION="connexion";
    public static final String DECONNEXION="deconnexion";
    public static final String MENU="menu";
    public static final String LISTE_MATCHS="liste_matchs";
    public static final String LISTE_PARIS="liste_paris";
    public static final String PARIER="parier";
    public static final String PARI_ANNULE="pari_annule";
    public static final String PARI_CONFIRMER="pari_confirmer";

    public static final String PAGE_CONNEXION = "/jsp/Connexion.jsp";
    public static final String PAGE_MENU = "/jsp/Menu.jsp";
    public static final String PAGE_LISTE_PARIS = "/jsp/ListeParis.jsp";
    public static final String PAGE_LISTE_MATCHS = "/jsp/ListeMatchs.jsp";
    public static final String PAGE_PARIER = "/jsp/Parier.jsp";
    public static final String PAGE_PARI_ANNULE = "/jsp/ParisAnnule.jsp";
    public static final String PAGE_PARI_CONFIRMER = "/jsp/ConfirmationPari.jsp";

    private FacadeParis facade;

    @Override
    public void init() throws ServletException{
        super.init();
        facade = new FacadeParisStaticImpl();
    }

    private String traiterConnexion(HttpServletRequest req){
        String destination;
        String login = req.getParameter("name");
        String pwd = req.getParameter("pwd");
        Utilisateur utilisateurConnecte;

        try{
            utilisateurConnecte = facade.connexion(login,pwd);
            req.getSession().setAttribute("user",utilisateurConnecte);
            destination = PAGE_MENU;
        } catch (UtilisateurDejaConnecteException udce){
            String erreur = "Utilisateur déjà connecté";
            req.setAttribute("erreur",erreur);
            destination = PAGE_CONNEXION;
        } catch (InformationsSaisiesIncoherentesException isie){
            String erreur = "Le login ou le mot de passe est incorrect";
            req.setAttribute("erreur",erreur);
            destination = PAGE_CONNEXION;
        }
        return destination;
    }

    private String traiterDeconnexion(HttpServletRequest req) {
        String destination;
        Utilisateur user = (Utilisateur) req.getSession().getAttribute("user");
        String login = user.getLogin();

        facade.deconnexion(login);
        req.getSession().invalidate();
        destination = PAGE_CONNEXION;
        return destination;
    }

    private String afficherMatchs(HttpServletRequest req){
        String destination = PAGE_LISTE_MATCHS;
        Collection<Match> listeMatch = facade.getAllMatchs();
        req.setAttribute("listeMatch", listeMatch);
        return destination;
    }

    private String afficherParis(HttpServletRequest req){
        String destination = PAGE_LISTE_PARIS;
        Utilisateur user = (Utilisateur) req.getSession().getAttribute("user");
        String login = user.getLogin();
        Collection<Pari> listeParis = facade.getMesParis(login);
        req.setAttribute("listeParis",listeParis);
        return destination;
    }

    private String annulerMonPari(HttpServletRequest req){
        String destination;
        Utilisateur user = (Utilisateur) req.getSession().getAttribute("user");
        String login = user.getLogin();
        long idMonPari = Long.valueOf(req.getParameter("idPari"));
        String monPari = req.getParameter("idPari");
        try{
            facade.annulerPari(login, idMonPari);
            destination = PAGE_PARI_ANNULE;
        } catch (OperationNonAuthoriseeException onae){
            String erreur = "Impossible d'annuler ce pari";
            req.setAttribute("erreur",erreur);
            destination = PAGE_LISTE_PARIS;
        }
        return destination;
    }

    private String parier(HttpServletRequest req){
        String destination;

        destination = PAGE_PARIER;

        return destination;
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String[] url = req.getRequestURI().split("/");
        String cleNavigation = url[url.length-1];
        String destination = PAGE_CONNEXION;

        switch (cleNavigation){
            case CONNEXION:
                destination = traiterConnexion(req);
                break;
        }

        req.getServletContext()
                .getRequestDispatcher(destination)
                .forward(req,resp);
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String[] url = req.getRequestURI().split("/");
        String cleNavigation = url[url.length-1];
        String destination = PAGE_CONNEXION;

        switch (cleNavigation){
            case DECONNEXION:
                destination = traiterDeconnexion(req);
                break;
            case MENU:
                destination = PAGE_MENU;
                break;
            case LISTE_MATCHS:
                destination = afficherMatchs(req);
                break;
            case LISTE_PARIS:
                destination = afficherParis(req);
                break;
            case PARIER:
                destination = PAGE_PARIER;
                break;
            case PARI_ANNULE:
                destination = annulerMonPari(req);
                break;
            case PARI_CONFIRMER:
                destination = parier(req); //user,id,vainqueur,montant);
                break;
        }

        req.getServletContext()
                .getRequestDispatcher(destination)
                .forward(req,resp);
    }
}