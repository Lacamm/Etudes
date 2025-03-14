<%--
  Created by IntelliJ IDEA.
  User: yoh
  Date: 04/01/2022
  Time: 17:26
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>My SHIFFUMI On LINE</title>
    <jsp:useBean id="messageErreurPartie" scope="request" type="java.lang.String" class="java.lang.String"/>
    <jsp:useBean id="messageErreurPseudo" scope="request" type="java.lang.String" class="java.lang.String"/>
</head>
<body>

<form action="/shiffumiOnLine/rejoindre" method="post">

    <label for="id:pseudo">Saisir votre pseudo</label> <input id="id:pseudo" type="text" name="pseudo">
    <label for="id:partie">Identifiant de la partie à rejoindre </label> <input id="id:partie" type="text" name="idPartie">
    <input type="submit">
</form>


<span style="color: red; ">
    ${messageErreurPseudo}
</span>



<span style="color: red; ">
    ${messageErreurPartie}
</span>



</body>
</html>
