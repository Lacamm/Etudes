#include <iostream>
#include <array>

// class : attribut privé
// struct : attribut public

// Si public ou private sont spécifiées, struct et class sont strictement équivalent
class toto
{
public:
    int a;
    int b;

private:
    float f;

public:
    toto()
    {
        a = 5;
    }

    class test
    {
    private:
        int a;
        int b;

    public:
        test()
        {
            a = b = 0;
        }
        void addOne()
        {
            a += 1;
            b += 1;
        }
    };

public:
    void method()
    {
        ++a;
    }
};


void fct(int &i) // Créer une copie de la valeur de i, pas i
{
    ++i;
}


int main()
{
    toto t0;
    t0.method();

    std::cout << t0.a << std::endl;

    int i = 3;
    fct(i);
    std::cout << i << std::endl;
    std::array<float, 5> a0 = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};

    for (std::size_t i = 0; i < a0.size(); ++i)
    {
        std::cout << a0[i] << std::endl;
    }

    std::string s0 = "abcdef";

    for (auto x : s0)
    {
        std::cout << x << std::endl;
    }

    std::cout << a0[10] << std::endl;
    std::cout << s0 + "xyz" << std::endl;
    //test test0;

    return 0;
}