<%--
  Created by IntelliJ IDEA.
  User: yoh
  Date: 10/01/2022
  Time: 13:38
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <jsp:useBean id="pseudo" type="java.lang.String" scope="session"/>
    <jsp:useBean id="idPartie" type="java.lang.String" scope="session"/>
    <title>Attente joueur</title>

    <script>
        function stateChange() {
            setTimeout(function () {
                var pathArray = window.location.pathname.split( "/" );
                var pathnamerebuilt="";
                for (let i=0;i<pathArray.length-1;i++) {
                    pathnamerebuilt+= pathArray[i]+"/";
                }
                var url = window.location.protocol + "//" + window.location.host + pathnamerebuilt + "attendre";
                window.location.replace(url);
            }, 4000);
        }
        stateChange()
    </script>
</head>
<body>


Bonjour ${pseudo}, nous attendons le second joueur pour la partie ${idPartie} !!!

<br>

<!--
<a href="/shiffumiOnLine/attendre">Refresh</a> -->

</body>
</html>
