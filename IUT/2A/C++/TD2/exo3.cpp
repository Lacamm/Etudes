
#include <iostream>
#include <array>
#include <cmath>

class Vec3f
{
private:
    std::array<float,3> v;

public:
    Vec3f(float x, float y, float z){
        v[0] = x;
        v[1] = y;
        v[2] = z;
    }

    Vec3f():Vec3f(0.0f,0.0f,0.0f){}

float & x()
{
    return v[0];
}

float x() const
{
    return v[0];
}

float length() const
{
    return std::sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]);
}

float & operator[](std::size_t i)
{
    return v[i];
}

float operator[](std::size_t i) const
{
    return v[1];
}

Vec3f & operator*=(float f)
{
    v[0]*=f;
    v[1]*=f;
    v[2]*=f;
    return *this;
}

Vec3f operator+(Vec3f const & v0)
{
    Vec3f tmp;
    tmp[0] = v[0]+v0[0];
    //tmp.v[0]
    tmp[1] = v[1]+v0[1];
    tmp[2] = v[2]+v0[2];
    return tmp;
}

Vec3f operator-(Vec3f const & v0)
{
    Vec3f tmp;
    tmp[0] = v[0]-v0[0];
    //tmp.v[0]
    tmp[1] = v[1]-v0[1];
    tmp[2] = v[2]-v0[2];
    return tmp;
}

bool operator<(Vec3f const v0)
{
    bool res;
    res = v[0]<v0[0];
    //tmp.v[0]
    res = v[1]<v0[1];
    res = v[2]<v0[2];
    return res;
}

Vec3f operator+=(Vec3f const v0)
{
    v[0]+=v0[0];
    v[1]+=v0[1];
    v[2]+=v0[2];
    return *this;
}

};

bool operator<(Vec3f const & v0, Vec3f const & v1)
{    
    return v0.length() < v1.length(); //appel length() car const
}

std::ostream & operator<< (std::ostream & out, Vec3f const & v)
{
    out << "[" << v[0] << ", " << v[1] << ", " << v[2];
    return out;
}

int main()
{
    Vec3f v0( 1.0f, 1.0f, 1.0f );
    Vec3f v1( 1.0f, 0.0f, 0.0f );

    v1.x() += 3.0f;
    v0[ 1 ] -= 1.0f;
    float l = v0.length();
    v1 *= l;
    auto v2 = v0 + v1;
    auto v3 = v0 - v1;

    if( v2 < v3 )
    {
        v2 += v3;
    }
    std::cout << v2 << std::endl;
    std::cout << v3 << std::endl;

    return 0;
}