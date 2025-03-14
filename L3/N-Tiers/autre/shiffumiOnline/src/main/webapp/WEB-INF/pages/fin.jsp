<%--
  Created by IntelliJ IDEA.
  User: yoh
  Date: 21/01/2022
  Time: 10:29
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Fin du jeu - Verdict</title>

    <jsp:useBean id="score" scope="request" type="modele.ScorePartie"/>
    <jsp:useBean id="verdict" type="java.lang.String" scope="request"/>

</head>
<body>
    <ul>
    <li> Hey ${pseudo} !</li>
    <li>Partie : ${idPartie}</li>
    <li>${score.joueurs[0]} vs ${score.joueurs[1]}</li>
    <li>${verdict}</li>
    </ul>


    <a href="/shiffumiOnLine/">Revenir à l'accueil</a>
</body>
</html>
