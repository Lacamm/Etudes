<%@ taglib prefix="s" uri="/struts-tags" %>
<%--
  Created by IntelliJ IDEA.
  User: o2184693
  Date: 04/02/2022
  Time: 15:25
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Résultats</title>
</head>
<body>
<div>
    <s:property value="operande1"/>
    <s:property value="symbole"/>
    <s:property value="operande2"/>
    <s:text name="egal">=</s:text>
    <s:property value="resultat"/>
</div>
<div>
    <s:a action="accueil"><s:text name="retourMenu"/></s:a>
</div>
</body>
</html>