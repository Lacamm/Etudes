<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Navigateur</title>
    </head>
    <body>
        <?php
        $AGENT=$_SERVER['HTTP_USER_AGENT'];
        echo $AGENT;
        echo ("\n<P>");
        if (stristr($AGENT,"MSIE"))
                echo "Vous semblez utiliser Internet explorer";
            elseif (preg_match("/Firefox/i", $AGENT))
                echo "Vous semblez utiliser Firefox";
                elseif (preg_match("/chrome/i",$AGENT))
                    echo "Vous semblez utiliser chrome";
                    elseif (preg_match("/Safari/",$AGENT))
                        echo "Vous semblez utiliser safari";
                    else echo "Navigateur inconnu"; 
        ?>
    </body> 
</html>