#include <iostream>
#include <array>

std::uint64_t facto(std::uint64_t n)
{
    return n < 2 ? 1 : n * facto(n - 1);
}

void fill(std::array<float, 10> &t0, float value)
{
    for (auto &x : t0) // Il faut passer la référence vers la donnée à modifier et pas une copie comme dans la version du dessus.
    {
        x = value;
    }
}

float maxtab(std::array<float, 10> const &t0)
{
    auto tmax = t0[0];
    for (std::size_t i = 1; i < t0.size(); ++i)
    {
        tmax = std::max(tmax, t0[i]); // tmax = tmax > t0[ i ] ? tmax : t0[ i ];
    }
    return tmax;
}


float sumtab(std::array<float, 10> const &t0)
{
    auto tsum = t0[0];
    for (std::size_t i = 1; i < t0.size(); ++i)
    {
        tsum += t0[i];
    }
    return tsum;
}


int main()
{
    //std::cout << facto(5) << std::endl;

    std::array<float, 10> t0;
    fill(t0, 1.0f);
    // for (auto x : t0)
    // {
    //     std::cout << x << std::endl;
    // }

    std::cout << maxtab(t0) << std::endl;

    std::cout << sumtab(t0) << std::endl;

    return 0;
}