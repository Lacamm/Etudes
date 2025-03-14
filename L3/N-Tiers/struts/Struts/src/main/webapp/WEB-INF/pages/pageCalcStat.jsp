<%@ taglib prefix="s" uri="/struts-tags" %>
<%--
  Created by IntelliJ IDEA.
  User: o2184693
  Date: 04/02/2022
  Time: 11:37
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Calculatrice Statique</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <h1><s:text name="calcStat.titre"/></h1>

    <s:form action="calcResStat">
        <s:textfield name="operande1" key="calcStat.operande1"/>
        <s:textfield name="operande2" key="calcStat.operande2"/>
        <s:select name="symbole" list="operateur"/>
        <s:submit key="calc.submit"/>
    </s:form>
    <div>
        <s:a action="accueil"><s:text name="retourMenu"/></s:a>
    </div>
</body>
</html>
