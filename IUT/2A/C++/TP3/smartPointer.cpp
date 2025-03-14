#include <iostream>
#include <memory>
#include <array>
#include <vector>

class toto
{
public:
    toto()
    {}
    toto( toto const & t) = delete;

    toto & operator=
};

class Personne
{
    friend std::ostream & operator<<(std::ostream & out, personne const & p);

private:
    std::string firstname;
    std::string lastname;

public:
    Personne(std::string const & firstname, std::string const & lastname): firstname(firstname), lastname(lastname) {}

};

std::ostream & operator<<(std::ostream & out, personne const & p)
{
    out << p.firstname <<' ' << p.lastname;
    return out
}

using uptr_personne = std::unique_ptr<personne>;

using array_pers = std::array<uptr_personne,10>;

int main(){

    array_pers personnes;

    for( std::size_t i = 0 ; i<personne.size(); i++ )
    {
        personnes[i] = std::make_unique<personne("a","b");
        std::cout*(personnes[i]) << std::endl;
    }
    personnes[3] ->firstname = "fdfdbfd";

    std::vector< uptr_personne> v0;
    v0.push_back(std::move(personnes[3]));

    std::cout << *(v[]) << std::endl;

    // toto t0;
    // toto t1(t0);
    // toto t2;
    // t1 = t2;

    retrun 0;
}