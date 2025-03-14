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

    <script>
        function stateChange() {
            setTimeout(function () {
                var pathArray = window.location.pathname.split( "/" );
                var pathnamerebuilt="";
                for (let i=0;i<pathArray.length-1;i++) {
                    pathnamerebuilt+= pathArray[i]+"/";
                }
                var url = window.location.protocol + "//" + window.location.host + pathnamerebuilt + "attente";
                window.location.replace(url);
            }, 4000);
        }
        stateChange()
    </script>

</head>
<body>

<ul>
    <li> Hey ${pseudo} !</li>
    <li>Partie : ${idPartie}</li>
    <li>${score.joueurs[0]} vs ${score.joueurs[1]}
    </li>
    <li>Score actuel : ${score.score.get(score.joueurs[0])} - ${score.score.get(score.joueurs[1])}</li>
    <li>Round : <jsp:getProperty name="score" property="nbRound"/></li>

</ul>



<b>On attend que votre adversaire joue !</b>









</body>
</html>
