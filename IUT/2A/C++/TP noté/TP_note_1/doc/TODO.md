# Sujet TP noté


Le fichier `test.cpp` contient du code qui doit être fonctionnel.
Ce code fait appel aux types suivants :

- `vml::vec3f` : un vecteur contenant 3 `float` (code donné),
- `vml::vec4f` : un vecteur contenant 4 `float` (à compléter),
- `vml::mat4x4f`: une matrice de dimensions 4x4 (à compléter), constituée de 4 vecteurs de type `vml::vec4f`, un vecteur représentant une colonne de la matrice.

Il est proposé de découper le travail en 4 étapes (Step 1, ...) à décommenter progressivement.
Il est conseillé de réfléchir avant de coder, notamment sur les opérateurs sur les matrices de manière à réutiliser au maximum les opérateurs déjà écrits. Par exemple, la multiplication d'une matrice par un vecteur peut réutiliser la multiplication d'un vecteur par une valeur de type `float`. De même, la multiplication de 2 matrices peut réutiliser la multiplication d'une matrice par un vecteur.

À partir de ces classes, on pourra définir des opérations de transformations géométriques : translation et rotation (code donné) dans le fichier `transform.hpp`. On obtient ainsi une petite bibliothèque similaire au sous-ensemble de fonctions de la bibliothèque `glm` utilisée en OpenGL.


Dans un second temps, il conviendra de déplacer des fonctions et méthodes dans des fichiers `.cpp`, dont la fonction `rotate` du fichier `transform.hpp`, les opérateurs `+` et `*` de la classe `vml::mat4x4f` et les opérateurs `<<` des autres classes. Une modification du fichier Makefile sera nécessaire pour compiler les nouveaux fichiers `.cpp` et générer le programme `test`.

La sortie du programme complet doit être :
```


v0
| 1 |
| 2 |
| 3 |
| 4 |

v1
| 1 |
| 1 |
| 7.5 |
| 1 |

v1*3.0f
| 3 |
| 3 |
| 22.5 |
| 3 |

v0*v1
29.5
v0
| 2 |
| 3 |
| 10.5 |
| 5 |

m0
| 0	0	0	0 |
| 0	0	0	0 |
| 0	0	0	0 |
| 0	0	0	0 |

m1
| 1	0	0	0 |
| 0	1	0	0 |
| 0	0	1	0 |
| 0	0	0	1 |

m0
| 2	0	0	0 |
| 3	0	0	0 |
| 10.5	0	0	0 |
| 5	0	0	0 |

m0
| 2	0	0	0 |
| 3	0	0	0 |
| 10.5	7	0	0 |
| 5	0	0	0 |

v2
| 4 |
| 6 |
| 42 |
| 10 |

m0 + m1
| 3	0	0	0 |
| 3	1	0	0 |
| 10.5	7	1	0 |
| 5	0	0	1 |

m0 * m1
| 4	0	0	0 |
| 6	0	0	0 |
| 21	14	0	0 |
| 10	0	0	0 |

r0*v3
| 0.707107 |
| -0.707107 |
| 0 |
| 1 |

| 1.70711 |
| -0.707107 |
| 0 |
| 1 |
```
