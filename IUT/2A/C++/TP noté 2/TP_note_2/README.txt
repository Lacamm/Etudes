Ce TP noté vise à montrer comment simplifier et avoir une approche de plus haut niveau en C++ pour le chargement de maillage vu en OpenGL qui est plutôt écrite en C.
Un tableau de points n'est plus vu comme : float * vertices mais comme un std::vector de vec3< float >, de même pour le tableau des normales. Le tableau d'indices est
 un std::vector< vec3< unsigned int > >.
La méthode load du fichier mesh.cpp effectue le chargement d'un fichier au format OFF et effectue le calcul des normales. La version proposée attend des opérateurs 
supplémentaire dans la classe template vec3 pour pouvoir fonctionner. Afin de proposer un code plus haut niveau on propose de remplacer toutes les boucles for de cette
 fonction par des algorithmes de la STL utilisant des lambdas.

Le TP noté se présente en 2 phases :

1. Ajouter les opérateurs, méthodes et fonctions nécessaires dans le fichier vec3.hpp pour que le projet compile.

2. Remplacer toutes les boucles for dans la fonction load du fichier mesh.cpp par des algorithmes de la STL avec utilisation de lambdas.

Pour tester le projet, une seule commande : make run.
L'exécution devrait afficher le contenu du tableau de normales.
