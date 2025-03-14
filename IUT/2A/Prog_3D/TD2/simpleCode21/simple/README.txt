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

brew install glm

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


Pour Windows: 
Pour installer les examples du td sous windows 10

Suivre les indications ici:

https://medium.com/@bhargav.chippada/how-to-setup-opengl-on-mingw-w64-in-windows-10-64-bits-b77f350cea7e


Adaptations à réaliser par rapport aux indications du site:
Utiliser :

glm-0.9.9.8
glew-2.1.0
freeglut-3.1.1


Pour  freeglut, glm, glew : il faut compiler avec cmake

Pour chacune des librairies: 

cmake -G "MinGW Makefiles" -S . -B . -DCMAKE_INSTALL_PREFIX=C:\mingw64\x86_64-w64-mingw32
mingw32-make all
mingw32-make install

Attention placer le répertoire glm obtenu dans c:\


Puis tester avec la nouvelle version de simple.zip du TD (la recharcher car je l'ai modifiée

Utiliser mingw32-make à la place de make 

