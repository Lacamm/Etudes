<!DOCTYPE html>
<html lang='fr'>
    <head>
        <meta charset="UTF-8">
        <link rel='stylesheet' href=''>
        <title></title>
    </head>
    <body>
        <p>L'adresse</p>
        <?php echo $_SERVER['REMOTE_ADDR'];?>
        <p>le nom du navigateur</p>
        <?php echo $_SERVER['HTTP_USER_AGENT'];?>
    </body>
</html>