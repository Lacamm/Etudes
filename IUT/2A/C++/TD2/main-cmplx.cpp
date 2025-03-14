#include <iostream>
#include <cmplx.hpp>

int main() {
    complex c0{ 1.0f, 2.0f };
    complex c1( -1.0f, 1.0f );
    c0.im =2.0f;
    auto c2 = c0 + c1;
    auto c3 = c0 * c1; // Attention à la mult. des nombres complexes.
    auto c4 = c0 - c1;
    c2.re += 3.0f;
    complex c5( c2 );
    std::cout << c0 << std::endl;
    std::cout << c1 << std::endl;
    std::cout << c2 << std::endl;
    std::cout << c3 << std::endl;
    std::cout << c4 << std::endl;
    std::cout << c5 << std::endl;
}