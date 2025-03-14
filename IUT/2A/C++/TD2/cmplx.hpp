#ifndef CPMLX_HPP
#define CPMLX_HPP

#include <iostream>
#include <array>

class complex
{
public:
    float re, im;

    complex(float re = 0.0f, float im = 0.0f) {};

    float operator[](std::size_t i) const
    {
        return i == 0 ? re : im;
    }
    float &operator[](std::size_t i)
    {
        return i == 0 ? re : im;
    }
};

complex operator+(complex const &c0, complex const &c1)
{
    return {c0.re + c1.re, c0.im + c1.im};
}

complex operator-(complex const &c0, complex const &c1)
{
    return {c0.re - c1.re, c0.im - c1.im};
}

complex operator*(complex const &c0, complex const &c1)
{
    return {c0.re*c1.re - c0.im*c1.im, c0.re*c1.im + c1.re*c0.im};
}

std::ostream &operator<<(std::ostream &out, complex const &c)
{
    out << "{ " << c.re << ", " << c.im << " }";
    return out;
}

#endif