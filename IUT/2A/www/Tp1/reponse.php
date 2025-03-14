<!DOCTYPE html>
<html lang='fr'>
    <head>
        <meta charset="UTF-8">
        <link rel='stylesheet' href=''>
        <title>Les reponses</title>
    </head>
    <body>
        <p>Voici les infos transmises:</p>
        <ul>
            <li>Votre nom:  
                <?php echo  $_POST['lenom'] ?>
            </li>
            <li>Reponse 1 :
                <?php
                $res = "Aucune réponse entrée";
                if(!empty($_POST['Hexakosioihexekontahexaphobie']) || !empty($_POST['JustinBieberphobie'])){
                    $res = "Faux";
                }
                if(!empty($_POST['Apopathodiaphulatophobie']) && empty($_POST['Hexakosioihexekontahexaphobie']) && empty($_POST['JustinBieberphobie'])){
                    $res = "Vrai";
                }
                echo $res;
                ?>
            </li>
            <li>Reponse 2 :
                <?php
                $res = "Aucune réponse entrée";
                if(!empty($_POST['Bubsy_3D']) || !empty($_POST['Angry_birds'])){
                    $res = "Faux";
                }
                if(!empty($_POST['Bugdom']) && empty($_POST['Bubsy_3D']) && empty($_POST['Angry_birds'])){
                    $res = "Vrai";
                }
                echo $res;
                ?>
            </li>
        </ul>
    </body>
</html>