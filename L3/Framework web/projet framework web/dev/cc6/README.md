# CC Framework Web 2021-2022

## Membres du groupes 
- VACHER Antoine
- BUDON Tom
- AVIGNON Alan
- ALLAIN Lucas


## Question 1

Pour créer le projet et mettre en place webpack encore et bootstrap, voici ce que nous avons fait :

On crée tout d'abord un projet avec `symfony new CCFW --full`

On installe ensuite webpack encore et bootstrap : 
```
symfony composer require symfony/webpack-encore-bundle
npm install
npm install bootstrap
```
Ensuite,on ajoute `import "bootstrap/dist/css/bootstrap.min.css"` dans la feuille de style dans assets/app.js.

Comme le contenu du fichier assets a été modifié, on utilise `npm run dev`.

Enfin, on ajoute dans config/packages/twig.yaml `form_themes: [ 'bootstrap_5_layout.html.twig' ]`.


## Question 2

On commence tout d'abord par décommenter la ligne `DATABASE_URL="sqlite:///%kernel.project_dir%/var/data.db"` dans le fichier .env.

Pour créer la base de données, on utilise la commande `symfony console doctrine:database:create`.
Ensuite, on crée l'entité Activité `symfony console make:entity Activite` et on ajoute le nom et la description à l'entité.
Pour créer la table, on utilise les commandes `symfony console make:migration` et `symfony console doctrine:migrations:migrate`.


## Question 3

On commence par installer le package fixture avec `symfony composer require orm-fixtures --dev`.
Ensuite on crée la fixtures via la commande symfony `console make:fixture`.
Puis, on peut utiliser Faker afin d'initialiser notre base de données.
Enfin, on utilise la commande `symfony console doctrine:fixtures:load`.


## Question 4

On lance la commande `symfony console make:crud`.

## Question 5

Nous n'avons pas utilisé de commande pour cette question.

## Question 6

Pour cette question nous avons suivi le cours proposé sur Celene.
En somme, nous avons utilisé Markdown directement dans le controlleur avant de créer une classe externe
afin de rendre le code plus léger. 
Enfin, nous avons ajouté dans le html l'instruction ` | raw ` après l'affichage de la description afin
de lire la valeur en tant que balise html.

## Question 7

On commence par créer l'utilisateur avec la commande `symfony console make:user`.

On utilise ensuite `symfony console make:entity User` afin d'ajouter le nom et le prénom à l'entité et on met a jour la base de données.

```
symfony console make:migration
symfony console doctrine:migrations:migrate
```

On crée ensuite le système d'authentification `symfony console make:auth`.

Enfin, on ajoute le systeme de création de compte `symfony console make:registration-form` et on met a jour notre fixtures afin de créer un utilisateur.

## Question 8

On va donc modifier l'entité User avec la commande `symfony console make:entity User`.
On crée ensuite une relation OneToMany avec l'entité Activité.
Après cela, on met à jour la base de données et la fixture.
```
symfony console make:migration
symfony console doctrine:migrations:migrate
symfony console doctrine:fixtures:load
```

## Question 9 

Pour ce faire, nous avons tout d'abord bloqué la création d'une activité pour les animateurs non connecté.

Nous avons ensuite modifié l'entité Activité avec la commande `symfony console make:entity Activite` pour lui ajouter un créateur.
Nous avons donc à nouveau crée une relation OneToMany avec l'entité User

Nous avons ensuite mis à jour la base de données ainsi que la fixture
```
symfony console make:migration
symfony console doctrine:migrations:migrate
symfony console doctrine:fixtures:load
```

## Question 10 

Nous avons décidé de restreindre l'édition et la suppression d'une activité. Seul son créateur sera capable de le faire.
Les autres utilisateurs ne pourront voir que les détails de l'activité pour le moment.
De plus, une personne non connectée ne pourra que se connecter, s'inscrire ou avoir la liste des activités.
Si la personne écrit le chemin dans la barre de recherche, elle sera renvoyée à la liste des activités.

Nous n'avons pas utilisé de commande Symfony pour mettre en place ces contraintes.

## Question 11

C Bô

## Question 12

On va donc modifier l'entité Activite avec la commande `symfony console make:entity Activite`.
On crée ensuite une relation ManyToMany avec l'entité User.
Après cela, on met à jour la base de données et la fixture.
```
symfony console make:migration
symfony console doctrine:migrations:migrate
symfony console doctrine:fixtures:load
```

Puis on ajoute les boutons d'inscription et de désinscription et les actions associées.

## Question 13

La liste des inscrits est dans les détails de l'activité. Ces inscriptions sont dans une nouvelle page.
Sinon, nous n'avons pas utilisé de commande pour cette question.






































