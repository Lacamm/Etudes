#include <iostream>

void echanger(int& a, int& b){
  int c = a;
  a = b;
  b = c;
}


int main(){

  std::cout << "Saisir une valeur : ";
  int a = 0;
  std::cin >> a;

  std::cout << "Saisir une valeur : ";
  int b = 0;
  std::cin >> b;

  std::cout << "Valeur 1 saisie : " << a << std::endl;
  std::cout << "Valeur 2 saisie : " << b << std::endl;

  std::cout << "Valeurs apres echange : " << std::endl;
  echanger(a,b);
  std::cout << "Valeur 1 échangée : " << a << std::endl;
  std::cout << "Valeur 2 échangée : " << b << std::endl;
  return 0;
}
