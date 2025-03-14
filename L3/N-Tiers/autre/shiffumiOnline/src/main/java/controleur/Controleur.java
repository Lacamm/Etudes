package controleur;

import modele.*;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Objects;

public class Controleur extends HttpServlet {

    public static final String GO_TO_CREATION="gotoCreation";
    public static final String GO_TO_REJOINDRE="gotoRejoindre";

    public static final String CREATION="creation";
    public static final String REJOINDRE="rejoindre";

    public static final String ATTENDRE="attendre";
    public static final String ATTENTE="attente";

    public static final String JOUER = "jouer";
    public static final String PAGE_DEFAUT = "/WEB-INF/pages/shiffumi.jsp";
    public static final String PAGES_ATTENTEJOUEUR_JSP = "/WEB-INF/pages/attentejoueur.jsp";
    public static final String PAGES_CREERPARTIE_JSP = "/WEB-INF/pages/creerpartie.jsp";
    public static final String PAGES_REJOINDREPARTIE_JSP = "/WEB-INF/pages/rejoindrepartie.jsp";
    public static final String PAGES_JOUER_JSP = "/WEB-INF/pages/jouer.jsp";
    public static final String PAGES_ATTENTEJEU_JSP = "/WEB-INF/pages/attentejeu.jsp";
    public static final String PAGES_FIN_JSP = "/WEB-INF/pages/fin.jsp";


    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String[] url = req.getRequestURI().split("/");
        // 1. On récupère la clé de navigation à partir de l'URI
        String cleNavigation = url[url.length-1];
        String destination  =PAGE_DEFAUT;
        // 2. Récupération de la façade si besoin
        // 3. Test selon la clé

        FacadeShiffumi facade = (FacadeShiffumi) getServletContext().getAttribute("facade");



        if (CREATION.equals(cleNavigation)) {

            String pseudo = req.getParameter("pseudo");
            String pseudInvite = req.getParameter("pseudoInvite");

            try {
                String cle = facade.creerPartie(pseudo,pseudInvite);
                req.getSession().setAttribute("idPartie",cle);
                req.getSession().setAttribute("pseudo",pseudo);
                destination= PAGES_ATTENTEJOUEUR_JSP;

            } catch (PseudosIncorrectsException e) {

                destination = PAGES_CREERPARTIE_JSP;
                String messageErreur="Problème avec les pseudos. Ils doivent être non-vides !!!";
                req.setAttribute("messageErreur",messageErreur);
            }

        }


        if (JOUER.equals(cleNavigation)) {
            String idPartie = (String) req.getSession().getAttribute("idPartie");
            try {

                ScorePartie scorePartie = facade.getScore(idPartie);
                req.setAttribute("score",scorePartie);
                req.getSession().setAttribute("roundCourant",scorePartie.getNbRound());
                // On enregistre le round courant pour vérifier lors de l'attente si l'autre a joué ou non
                String choix = req.getParameter("choixJoueur");

                facade.jouer((String) req.getSession().getAttribute("pseudo"),idPartie, FacadeShiffumi.Coups.valueOf(choix));

                destination = PAGES_ATTENTEJEU_JSP;

            } catch (PartieInexistanteException e) {
                destination = PAGE_DEFAUT;
            } catch (PseudoInconnuDansLaPartieException e) {
                destination = PAGE_DEFAUT;
            } catch (DejaJoueException e) {
                destination = PAGE_DEFAUT;

            } catch (PartieTermineeException e) {
                destination= PAGES_FIN_JSP;
                ScorePartie scorePartie = null;
                try {
                    scorePartie = facade.getScore(idPartie);
                    req.setAttribute("score",scorePartie);
                } catch (PartieInexistanteException ex) {
                    ex.printStackTrace();
                }
            }

        }

        if (REJOINDRE.equals(cleNavigation)) {

            String pseudo = req.getParameter("pseudo");
            String idPartie = req.getParameter("idPartie");

            try {
                facade.rejoindrePartie(pseudo,idPartie);
                req.getSession().setAttribute("idPartie",idPartie);
                req.getSession().setAttribute("pseudo",pseudo);
                destination= PAGES_ATTENTEJOUEUR_JSP;

            }
            catch (PseudoInconnuDansLaPartieException e) {
                destination = PAGES_REJOINDREPARTIE_JSP;
                String messageErreur="Le pseudo renseigné est inconnu !!!";
                req.setAttribute("messageErreurPseudo",messageErreur);

            } catch (PartieInexistanteException e) {
                destination=PAGES_REJOINDREPARTIE_JSP;
                String messageErreur="Partie Inexistante !!!";
                req.setAttribute("messageErreurPartie",messageErreur);
            }

        }





        // 5. Redirection
        req.getServletContext()
                .getRequestDispatcher(destination)
                .forward(req,resp);

    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        String[] url = req.getRequestURI().split("/");
        // 1. On récupère la clé de navigation à partir de l'URI
        String cleNavigation = url[url.length-1];
        String destination  =PAGE_DEFAUT;
        // 2. Récupération de la façade si besoin

        FacadeShiffumi facadeShiffumi = (FacadeShiffumi) getServletContext().getAttribute("facade");
        // 3. Test selon la clé
        if (GO_TO_CREATION.equals(cleNavigation)) {
            destination = PAGES_CREERPARTIE_JSP;
            // 4. Traitement sur les données
        }

        if (GO_TO_REJOINDRE.equals(cleNavigation)) {
            destination = PAGES_REJOINDREPARTIE_JSP;
            // 4. Traitement sur les données
        }



        if (ATTENDRE.equals(cleNavigation)) {
            String idPartie = (String) req.getSession().getAttribute("idPartie");
            if (facadeShiffumi.isPartieCommencee(idPartie)) {
                req.setAttribute("coupsPossibles",facadeShiffumi.getCoupsPossibles());
                try {
                    req.setAttribute("score",facadeShiffumi.getScore(idPartie));
                } catch (PartieInexistanteException e) {
                    e.printStackTrace();
                }
                destination = PAGES_JOUER_JSP;
            }
            else {
                destination=PAGES_ATTENTEJOUEUR_JSP;
            }

        }

        if (ATTENTE.equals(cleNavigation)) {
            String idPartie = (String) req.getSession().getAttribute("idPartie");
            int nbRound = (int) req.getSession().getAttribute("roundCourant");
            // On récupère le round courant que l'on avait stocké avant de jouer et on vérifie
            // s'il a changé. Si c'est cas, les deux joueurs ont joué

            ScorePartie scorePartie = null;
            try {
                scorePartie = facadeShiffumi.getScore(idPartie);
            } catch (PartieInexistanteException e) {
            }
            if (Objects.nonNull(scorePartie)) {

                try {
                    if (scorePartie.getNbRound() != nbRound) {

                        if (facadeShiffumi.isPartieTerminee(idPartie)) {
                            req.setAttribute("score", scorePartie);
                            String gagnant = scorePartie.getGagnant();
                            req.setAttribute("verdict", "Le gagnant est " + gagnant);
                            destination = PAGES_FIN_JSP;
                        } else {
                            req.setAttribute("coupsPossibles", facadeShiffumi.getCoupsPossibles());
                            req.setAttribute("score", scorePartie);
                            destination = PAGES_JOUER_JSP;
                        }
                    } else {
                        req.setAttribute("score", scorePartie);
                        destination = PAGES_ATTENTEJEU_JSP;
                    }
                } catch(PartieInexistanteException e){
                    destination = PAGE_DEFAUT;
                } catch(MatchNulException e){
                    req.setAttribute("score", scorePartie);
                    req.setAttribute("verdict", "Aucun vainqueur, bravo aux deux joueurs !");
                    destination = PAGES_FIN_JSP;

                } catch(PartieNonTermineeException e){
                    e.printStackTrace();
                }
            }
            else {
                destination = PAGE_DEFAUT;
            }
        }


        // 5. Redirection
        req.getServletContext()
                .getRequestDispatcher(destination)
                .forward(req,resp);
    }
}
