<!doctype html>
<html>
<head>
<title>
Connexion à MySQL avec PDO
</title>
<meta charset="utf-8">
<link rel="stylesheet" href="tabstyle.css" />
</head>
<body>
<h1>
Interrogation de la table CARNET avec PDO
</h1>

<?php
require_once('connexion.php');
$connexion=connect_bd();
$sql="SELECT * from CARNET";
if(!$connexion->query($sql)) echo "Pb d'accès au CARNET";
else{
?>
<form action="recherche.php" method="GET">
    	<select name="ID">
      <?php
      foreach ($connexion->query($sql) as $row)
      if(!empty($row['NOM']))
    	echo "<option value='".$row['ID']."'>"
        .$row['PRENOM']." ".$row['NOM']."</option>\n";
      ?>
     </select>
     <input type="submit" value="Rechercher">
     </form>
     <?php 
      } 
     ?>
</body>
</html>