<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<%--
  Created by IntelliJ IDEA.
  User: yoh
  Date: 10/01/2022
  Time: 14:15
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Shiffumi On LINE !! </title>
    <jsp:useBean id="score" scope="request" type="modele.ScorePartie"/>
    <jsp:useBean id="pseudo" scope="session" type="java.lang.String"/>
    <jsp:useBean id="idPartie" scope="session" type="java.lang.String"/>
    <jsp:useBean id="coupsPossibles" scope="request" type="java.util.Collection<java.lang.String>"/>
</head>
<body>

<ul>

    </li>

    <li>Round : <jsp:getProperty name="score" property="nbRound"/></li>

    <li>Score actuel : ${score.score.get(score.joueurs[0])} - ${score.score.get(score.joueurs[1])}</li>



    <form action="/shiffumiOnLine/jouer" method="post">
        <label for="id:choixJoueur">Choisir :</label>
        <select id="id:choixJoueur" name="choixJoueur">

            <c:forEach items="${coupsPossibles}" var="coups">
            <option>${coups}</option>
        </c:forEach>
        </select>
        <input type="submit">
    </form>
</ul>










</body>
</html>
