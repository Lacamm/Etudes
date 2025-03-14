<%--
  Created by IntelliJ IDEA.
  User: o2184693
  Date: 17/01/2022
  Time: 09:38
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Paris en ligne</title>
</head>
<body>
    <p><?php echo $_SERVER["PHP_AUTH_USER"]; ?></p>
    <p>Vous avez parié {{ }}€ sur le résultat {{ }} pour le match: {{ }}</p>
    <a href="/pel/menu">Retour au menu</a>
</body>
</html>
