#include <iostream>

class Personne
{
/*
L'opérateur << est ami de la classe donc peut accéder aux attributs privés.
*/
friend std::ostream & operator<<( std::ostream & out, Personne & p0 );

private:
  std::string nom, prenom;
  std::uint64_t id;
  static std::uint64_t count;

public:
  Personne( std::string nom, std::string prenom ): nom(nom), prenom(prenom)
  {
    id = count++;  
  }
};

std::uint64_t Personne::count = 0;

std::ostream & operator<<( std::ostream & out, Personne & p0 )
{
  out << p0.nom << " " << p0.prenom << " " << p0.id;
  return out;
}

int main()
{
  Personne p0( "toto", "toto" );
  std::cout << p0 << std::endl;
  return 0;
}