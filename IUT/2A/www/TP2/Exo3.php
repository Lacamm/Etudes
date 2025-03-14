<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <?php
            echo inverserChaine("C'est beau hein !");
            echo "</br>";
            estPalindrome("kayak");
            echo "</br>";
            estPalindrome("banane");
            echo "</br>";

        ?>
        
        <?php
            function inverserChaine($str){
                return strrev($str);
            }
        ?>

        <?php
            function estPalindrome($str){
                $var = strrev($str);
                if ($var==$str){
                    echo "C'est un palindrome";
                }
                else{
                    echo "Ce n'est pas un palindrome";
                }
            }
        ?>

        <?php
            function nbOccurences($str, $var){
                $total = 0;
                for ($i=0;strlen($str);strlen($var)) {
                    $morceau = substr
                    if ($var == ){

                    }
                }   
            }
        ?>

    </body> 
</html>