<%--
  Created by IntelliJ IDEA.
  User: o2184693
  Date: 17/01/2022
  Time: 08:51
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Connectez-vous</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <jsp:useBean id="erreur" class="java.lang.String" scope="request"/>
</head>
<body>
    <form action="/pel/connexion" method="post" class="">
        <div class="">
            <label> Pseudo: </label>
            <input type="text" name="name" id="name" required>
        </div>
        <div class="">
            <label> Mot de passe: </label>
            <input type="password" name="pwd" id="pwd" required>
        </div>
        <div class="">
            <input type="submit" value="Connexion">
            ${erreur}
        </div>
    </form>
</body>
</html>
