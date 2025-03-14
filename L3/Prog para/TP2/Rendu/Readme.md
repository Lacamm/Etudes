ALLAIN Lucas - Boulanger + Couper les coins

Instructions :

1) Extraire l'archive et copier le fichier "backer.c" dans le répertoire "easypap/kernel/c"
2) Ce Placer dans le répertoire "easypap", faire "make" dans un terminal
3) Faire les commandes: "./run --kernel baker --variant seq -i 1000 -l ./images/index.png -du" pour enregistrer l'image du gateau complete avec le kernel baker.c après 1000 itérations
			"./run --kernel baker --variant omp -i 1000 -l ./images/index.png --monitoring" pour l'image du gateau complete avec le kernel baker.c après 1000 itérations et visualisation de l'utilisation du CPU
			"./run --kernel baker --variant tiled -i 1000 -l ./images/index.png --no-display" pour l'image du gateau complete avec le kernel baker.c après 1000 itérations sans l'afficher mais avec le temps d'execution en milisecondes

4) Pour tester les tuiles :
./run --kernel baker --variant tiled -i 1000 -l ./images/index.png -n
./run --kernel baker --variant omp_tiled -i 1000 -l ./images/index.png -n
./run --kernel baker --variant omp_task_tiled -i 1000 -l ./images/index.png -n

./run --kernel baker --variant corners_tiled -i 126661429 -l ./images/index.png -n

Description des kernels : 

Les kernels permettent de définir de calculs sur des images, ici on a "baker" qui itére un certain nombre de fois sur une image en faisant "tourner les pixels" avant d'arriver à l'image finale

Description des variants :

Les variants sont différents moyen d'appliquer la parallélisation a un kernel

"baker_compute_seq" avec "transformation" : Version séquentielle du kernel baker
"baker_compute_omp" avec "transformation" : Version parallélisée du kernel baker
"baker_compute_tiled" avec "transformation" : Version avec les tuiles du kernel baker
"baker_compute_omp_tiled" avec "do_tile" et "transformation" : Version parallélisée avec les tuiles du kernel baker
"baker_compute_omp_task" avec "transformation" : Version parallélisée avec les tasks du kernel baker
"baker_compute_omp_task_tiled" avec "transformation" : Version parallélisée avec les tasks et les tuiles du kernel baker

"baker_compute_corners" avec "apply_pixel_cycle" : Version séquentielle de couper les bords
"baker_compute_corners_omp" avec "apply_pixel_cycle" : Version parallélisée de couper les bords
"baker_compute_corners_omp_task" avec "apply_pixel_cycle" : Version parallélisée de couper les bords avec tasks
"baker_compute_corners_tiled" avec "do_tile" : Version avec les tuiles
"baker_compute_corners_omp_tiled" avec "do_tile"Version parallélisée avec les tuiles
"baker_compute_corners_omp_task_tiled" avec "do_tile" : Version parallélisée avec les tuiles et tasks


