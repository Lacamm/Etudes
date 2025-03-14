Ce cours s’appuie essentiellement sur https://developer.android.com/training/data-storage/room

Telecharger l’application BD1920, importez la dans android studio puis testez.


Voici comment réaliser cette application:

1- Créer un nouveau projet. Dans le cas de cet exemple, on a utilise une Basic Activity en utilisant android x.

2- Importer les dépendances nécessaires.
Cf diapos 7-8
Dans l’application, mise a jour du fichier build.gradle (Module: app)

3- Definition des entités
Cf diapos 9-20
Dans l’application, creation d’un nouveau package Models puis d’une nouvelle classe Word.
Ici, c’est un exemple très simple. Normalement, il aurait fallu au moins un identifiant, …

Pour le moment, nous n’avons qu’une seule table. Pour votre projet, nous demandons plusieurs tables avec des relations. Pour cela, vous pourrez regarder:
https://developer.android.com/training/data-storage/room/relationships

4- Mise en place des DAOs. 
C’est les objets qui vont permettre de manipuler la BD.
Cf diapos 21-33
Attention a l’utilisation des LiveDatas. Voire explication dans le cours. On y reviendra un peu plus tard.
Dans l’application, package BDD, WordDao.

5- RoomDatabase
C’est la classe qui permet l’acces a la BD.
Pour chaque application, une BD SQLlite est disponible.
Cf diapos 34-36
Dans l’application, package BDD, WordRoomDatabase. Utilisation du pattern singleton que vous connaissez.

6- Le Repository
Nécessaire pour fournir une API a notre application en lien avec la BD.
Attention, les requêtes doivent s’effectuer dans un autre thread => utilisation des AsyncTasks
https://developer.android.com/reference/android/os/AsyncTask

 Dans l’application, package BDD, WordRepository.

7- ViewModel
Cf diapos 39-40
https://developer.android.com/topic/libraries/architecture/viewmodel

Dans l’application, package BDD, WordViewModel.

8- Ajout d’une nouvelle activité (NewWordActivity) et Modification/Ajout des différents layout nécessaires. Cf res/layout
Attention, ajout de ressources dans values/dimens, strings, colors et styles

9- Ajout de la classe WordListAdapter pour une RecyclerView dans le package Tools de l’application avec le layout recyclerview_item.
Deja vu en TD/TP

10- Finalisation des deux activités.
Attention, dans MainActivity, creation du WordViewModel, ajout des observer sur les LiveData.
