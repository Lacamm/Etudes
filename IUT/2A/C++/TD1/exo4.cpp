#include <iostream>

class A
{
private: // Pas indispensable car on fait une classe donc tout est privé par défaut.
    int a, b;

public:
    A()
    {
        a = b = 0;
    }//A() : a(0), b(0) {} // Autre notation possible utilisant les constructeurs de a et b.

    ~A()
    {
        std::cout << "Destructeur de A\n" << std::endl;
    }

    void addOne()
    {
        ++a; // Idem que a+=1;
        ++b;
    }

public:
    A(int x, int y)
    {
        a = x;
        b = y;
    }

    int getA() const
    {
        return a; // retourne une copie.
    }
    int &getA()
    {
        return a; // retourne a par référence.
    }
    int getB() const
    {
        return b;
    }
    void display()
    {
        std::cout << getA() << std::endl;
        std::cout << getB() << std::endl;
    }

    A operator+(A const &a0) const
    {
        A tmp;
        tmp.a = this->a + a0.a;
        tmp.b = this->b + a0.b;
        return tmp;
    }
};

std::ostream & operator<<( std::ostream & out, A const & a0 )
{
  out << a0.getA() << " " << a0.getB();
  return out;
}

int main()
{
    //A a0(5,8); // Pas de new comme en Java. L'instance a0 est mise dans la pile.
    A a0(3,4);
    std::cout << a0 << std::endl;
    
    std::cout << a0 << std::endl;
    a0.addOne();
    //a0.display();

    //std::cout << a0.getA() << std::endl;
    a0.getA() += 5;


    return 0;
}
