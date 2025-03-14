<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Les reponses</title>
    </head>
    <body>
        <p>Voici les infos transmises</p>
            <ul>
                <li>Votre nom:
                    <?php echo $_POST['lenom']; ?>
                </li>
                <li>Reponse 1 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['zigoui']) || !empty($_POST['zigou'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['zizi']) && empty($_POST['zigou']) && empty($_POST['zigoui'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>
                </li>
                <li>Reponse 2 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['Danemark']) || !empty($_POST['Finlande'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['Norvege']) && empty($_POST['Finlande']) && empty($_POST['Danemark'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>
                </li>
                <li>Reponse 3 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['Guillaume']) || !empty($_POST['Dylan'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['Leo']) && empty($_POST['Dylan']) && empty($_POST['Guillaume'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>
                </li>
                <li>Reponse 4 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['Shangai']) || !empty($_POST['Pékin'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['Tokyo']) && empty($_POST['Shangai']) && empty($_POST['Pékin'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>
                </li>
                <li>Reponse 5 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['Pierre']) || !empty($_POST['Marie'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['Philippe']) && empty($_POST['Pierre']) && empty($_POST['Marie'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>
                </li>
                <li>Reponse 6 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['39']) || !empty($_POST['17'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['28']) && empty($_POST['39']) && empty($_POST['17'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>
                </li>
                <li>Reponse 7 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['Alpes']) || !empty($_POST['Bouches'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['Vaucluse']) && empty($_POST['Alpes']) && empty($_POST['Bouches'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>
                </li>
                <li>Reponse 8 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['Poires']) || !empty($_POST['Citrons'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['Pommes']) && empty($_POST['Poires']) && empty($_POST['Citrons'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>
                </li>
                <li>Reponse 9 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['jaune']) || !empty($_POST['violet'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['blanc']) && empty($_POST['jaune']) && empty($_POST['violet'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>
                </li>
                <li>Reponse 10 :
                    <?php
                    $res = "Aucune réponse entrée";
                    if(!empty($_POST['Vénus']) || !empty($_POST['Athéna'])){
                        $res = "Faux";
                    }
                    if(!empty($_POST['Aphrodite']) && empty($_POST['Vénus']) && empty($_POST['Athéna'])){
                        $res = "Vrai";
                    }
                    echo $res;
                    ?>  
                </li>
            </ul>
    </body> 
</html>