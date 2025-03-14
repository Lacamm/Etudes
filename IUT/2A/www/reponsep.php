<!DOCTYPE html>
<html lang='fr'>
    <head>
        <meta charset="UTF-8">
        <link rel='stylesheet' href='stylep.css'>
        <title>Les reponses</title>
    </head>
    <body>
        <p>Voici les infos transmises:</p>
        <ul>
            <li>Votre nom:  
                <?php echo $_POST['lenom']; ?>
            </li>
            <li>Votre adresse mail:  
                <?php echo $_POST['mail']; ?>
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
                if ($_POST['Bugdom']){
                    $_res = 'Vrai';
                }
                // if(!empty($_POST['Jeux']) == 'Bugdom' && empty($_POST['Jeux']) == 'Angry_birds' && empty($_POST['Jeux']) =='Bubsy_3D' ){
                //     $res = "Vrai";
                // }
                else{
                    $_res = "Faux";
                }
                echo $res;
                ?>
            </li>
        </ul>
    </body>
</html>