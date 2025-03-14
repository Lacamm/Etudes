<!doctype html>
<html>
    <head>
        <title>
        Connexion à MySQL avec PDO
        </title>
    <meta charset="utf-8">
    </head>

    <body>
        <?php

        $res = "Aucune personne sélectionnée";
        if(!empty($_POST['DURAND']) && !empty($_POST['DURAND'])){
            $res="SELECT * from CARNET where NOM='DURAND' and PRENOM='JEAN'";
        }
        if(!empty($_POST['SMITH']) && !empty($_POST['JOHN'])){
            $res="SELECT * from CARNET where NOM='SMITH' and PRENOM='JOHN'";
        }
        echo $res;
        ?>
    </body>
</html>