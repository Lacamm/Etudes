#include <iostream>

void fct(int *p)
{
    *p += 2;
}

int main()
{
    int a = 5;
    int *p_a = &a;
    *p_a += 3;
    fct(p_a);
    std::cout << a << std::endl;
    return 0;
}