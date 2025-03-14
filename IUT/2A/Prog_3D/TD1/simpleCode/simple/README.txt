Pour compiler ce caneva:

installer les paquetages suivants:

sudo apt-get  install  cmake freeglut3-dev build-essential
sudo apt-get install libglew-dev
sudo apt-get install -y libglm-dev

puis: 
mkdir BUILD
cd BUILD
cmake ..
make 


Pour executer:
make check

ou bien:
./exo_3D



Pour MAC OSX 10.15:

brew install cmake


puis: 
mkdir BUILD
cd BUILD
cmake ..
make 


Pour executer:
make check

ou bien:
./exo_3D

Ou bien utiliser Xcode:

mkdir BUILD
cd BUILD
cmake -G Xcode ..

Et vous avez un environement avec l'IDE Xcode


Pour Windows: Certains étudiants en 2020 de l'IUTO ont réussi à faire tourner ce code via Cmake dans VisualStudio.  Ce n'est pas une légende, j'en ai été témoin.





