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
    <jsp:useBean id="listeParis" type="java.util.Collection<modele.Pari>" scope="request"/>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
    <ul>
        <c:forEach items="${listeParis}" var="x">
            <li>Pari n&deg;${x.idPari}
                - ${x.match}
                - ${x.vainqueur}
                - ${x.montant}
                <a href="/pel/pari_annule?idPari=${x.idPari}">Annuler</a></li>
        </c:forEach>
    </ul>
    <a href="/pel/menu">Retour au menu</a>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
