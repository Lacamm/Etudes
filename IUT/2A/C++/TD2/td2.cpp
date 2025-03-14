#include <iostream>

class Test
{
private:
    int a;
public:
    Test(): a(0)
    {}
    Test( Test const & t ) //recopie
    {
        a = t.a;
    }
    Test( int a ): a(a){} // ou arg init avec une valeur

    Test & operateur=(Test const & t)
    {
        std::cout << "operator\n";
        a = t.a;
        return *this;
    }
    
};

int main()
{
    Test t0;
    std::cout << t.a << std::endl;
    Test t1(t0); // constructeur de recopie
    std::cout << t.a << std::endl;

    Test t2 = t1; // équivalent à t2(t1)
    std::cout << t2.a << std::endl;
    // t0 = (t2 = t1) t0.operator=(t2.operator=(t1))
    t0 = t2; // operateur =
    std:: cout << t0.a << std::endl

    return 0;
}