<?php

date_default_timezone_set('Europe/Paris');
try{
  // le fichier de BD s'appellera contacts.sqlite
  // on cree un répertoire /tmp dans notre www
  // avec le droit d'écriture pour tout le monde:
  //    mkdir tmp
  //    chmod a+rwX tmp 
  //$file_db=new PDO('sqlite:./tmp/contacts.sqlite');
  $file_db=new PDO('mysql:./tmp/contacts.sql');
  $file_db->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_WARNING);
  $file_db->exec("CREATE TABLE IF NOT EXISTS contacts ( 
 id INTEGER PRIMARY KEY,
 nom TEXT,
 prenom TEXT,
 time INTEGER)");
  
  $contacts=array(
		  array('nom' => 'De Guillemets',
			'prenom' => 'Virgule',
			'time' =>  strtotime('22-09-2008')),
		  array('nom' => 'Talon',
			'prenom' => 'Achille',
			'time' =>  strtotime('12-09-2013')),
		  array('nom' => 'Higgs',
			'prenom' => 'Peter',
			'time' =>  strtotime('24-09-2014'))
		  );
		  
  $insert="INSERT INTO contacts (nom, prenom, time) VALUES (:nom, :prenom , :time)";
  $stmt=$file_db->prepare($insert);
  // on lie les parametres aux variables
  $stmt->bindParam(':nom',$nom);
  $stmt->bindParam(':prenom',$prenom);
  $stmt->bindParam(':time',$time);

  foreach ($contacts as $c){
    $nom=$c['nom'];
    $prenom=$c['prenom'];
    $time=$c['time'];
    $stmt->execute();
  }
  
  echo "Insertion en base reussie !";
  // on va tester le contenu de la table contacts
  $result=$file_db->query('SELECT * from contacts');
  foreach ($result as $m){
    echo "<br/>\n".$m['prenom'].' '.$m['nom'].' '
    .date('Y-m-d H:i:s',$m['time']);
  }
  // on ferme la connexion
  $file_db=null;
}
catch(PDOException $ex){
  echo $ex->getMessage();
}