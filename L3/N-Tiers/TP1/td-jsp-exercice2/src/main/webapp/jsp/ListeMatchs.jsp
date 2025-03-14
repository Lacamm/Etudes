<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: o2184693
  Date: 17/01/2022
  Time: 09:21
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Paris en ligne</title>
    <jsp:useBean id="listeMatch" type="java.util.Collection<modele.Match>" scope="request"/>
</head>
<body>
    <ul>
        <c:forEach items="${listeMatch}" var="x">
            <li>Match n&deg;${x.idMatch}
                - ${x.sport}
                - ${x.quand}
                - ${x.equipe1} vs ${x.equipe2}
            <a href="/pel/parier?idMatch=${x.idMatch}">Parier</a></li>
        </c:forEach>
    </ul>
    <a href="/pel/menu">Retour au menu</a>
</body>
</html>
