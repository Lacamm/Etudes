#include <iostream>
#include <vector>

int main()
{
    vector<int> v1(10);
    v1[0] = 5;
    for (unsigned int i = 0; i < 10; ++i)
    {
        v1.push_back(rand() % 100);
    }
    std::cout << "Taille = " << v1.size() << std::endl
         << "  ";
    for (unsigned int i = 0; i < v1.size(); ++i)
    {
        std::cout << v1[i] << ' ';
    }
    std::cout << std::endl;
}