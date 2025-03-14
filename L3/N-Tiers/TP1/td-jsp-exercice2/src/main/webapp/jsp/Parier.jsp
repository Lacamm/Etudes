<%--
  Created by IntelliJ IDEA.
  User: o2184693
  Date: 17/01/2022
  Time: 09:37
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Paris en ligne</title>
</head>
<body>
    <form action="pari_confirmer" method="post" class="">

        <p>Résultat pour le match: {{ }}</p>
        <div>
            <input type="radio" id="gagnant1" name="drone" value="gagnant1" checked>
            <label for="gagnant1">{{Equipe 1}} - Gagnant</label>
        </div>
        <div>
            <input type="radio" id="gagnant2" name="drone" value="gagnant2">
            <label for="gagnant2">{{Equipe 2}} - Gagnant</label>
        </div>
        <div>
            <input type="radio" id="nul" name="drone" value="nul">
            <label for="nul">Match Nul</label>
        </div>
        <div class="">
            <label> Montant: </label>
            <input type="number" name="pari" id="pari" required>
        </div>
        <div class="">
            <input type="submit" value="Valider">
        </div>
    </form>
</body>
</html>
