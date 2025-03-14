<?php
  header("Content-Type: application/json");
   if (!empty($_REQUEST['cp'])){
     $cp = $_REQUEST['cp'];
     setLocale(LC_TIME,"fr_FR.utf8");
     date_default_timezone_set("Europe/Paris");
     $today = strftime('%A %d %B %y',time());
     $hour = date('H:i:s');
     $meteo = array("cp"=>$cp,
                    "jour"=>$today, 
                    "heure"=> $hour,
                    "meteo"=>"Il va faire très beau !" );
     if ($cp=='45000') {
        $meteo['meteo'] = "Averses";
        echo json_encode($meteo,JSON_PRETTY_PRINT);
     }
     elseif ($cp=='13000') 
        echo json_encode($meteo,JSON_PRETTY_PRINT);
     elseif ($cp=='06000') 
        echo json_encode($meteo,JSON_PRETTY_PRINT);
     else echo json_encode("Code postal inconnu");
   }
   else echo json_encode("Précisez le code postal !!");