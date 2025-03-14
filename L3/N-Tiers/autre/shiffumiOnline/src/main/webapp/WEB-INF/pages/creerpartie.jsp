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
    <jsp:useBean id="messageErreur" scope="request" type="java.lang.String" class="java.lang.String"/>

    <title>My SHIFFUMI On LINE</title>
</head>
<body>

<form action="/shiffumiOnLine/creation" method="post">

    <label for="id:pseudo">Saisir votre pseudo</label> <input id="id:pseudo" type="text" name="pseudo">
    <label for="id:invite">Saisir le pseudo de votre invité</label> <input id="id:invite" type="text" name="pseudoInvite">
    <input type="submit">
</form>




<span style="color: red; ">
${messageErreur}
</span>


</body>
</html>
