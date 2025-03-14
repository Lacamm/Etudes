#include <iostream>
#include <vector>
#include <array>
#include <list>
#include <map>

std::ostream & operator<<(std::ostream & out ), std::vector<float> const & v)
{
    for (auto x:v)
    {
        out << x << std::endl;
    }
    return out;
}

template <typename T>
T maxi( T a, T b )
{
    return a > b ? a : b;
}



int main()
{
    std::vector<float> v(10);

    std::generate(v.begin(), v.end(), [](){ return std::rand()%10/10.0f;}
    );

    float scale = 2.0f;

    auto lambda = [](){return 5;};

    std::cout << lambda() << std::endl;

    std::for_each(v.begin(), v.end(), [&tmp,scale](float f)
    {tmp += f*f*scale;});


    // std::array<flaot, 20> v;
    // for(auto x:v)
    // {
    //     std::cout << x <<std::endl;
    // }


    // std::vector<float> v(10);
    // v->push_back(1.0f);

    // v[5] = 3.0f;
    // std::cout << v << std::endl;

    // for(auto x:v)
    // {
    //     std::cout << x << std::endl;
    // }
   

    // auto n0 = maxi(1.5f, 2.6f);
    // auto n1  = maxi(4, 2);

    // std::cout << n0 << std::endl;
    // std::cout << n1 << std::endl;

    return 0;
}