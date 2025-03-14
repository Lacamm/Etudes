#include <iostream>

class vecf
{
private:
    std::size_t s;
    float * p;

public:
    vecf(std::size_t size): //constructeur 1
        s(size),
        p(new float[size])
    {}

    vecf(vecf const & v): //constructeur 2
        vecf(v.s)
    {
        for ( std::size_t i=0; i<s; i++)
        {
            p[i] = v.p[i];
        }
    }

    ~vecf() //destructeur
    {
        delete [] p;
    }

    vecf operator=(vecf const & v) //operateur =
    {
        if(this != &v)
        {
            delete [] p;
            s = v.s;
            p = new float[v.s];
            //p = newfloat(10)
            for(std::size_t i = 0; i < s; i++)
            {
                p[i] = v.p[i];
            }
        }
        return *this;
    }

    float operator[](std::size_t i) const//copie pas modifiable : copie
    {
        return p[i];
    }

    float & operator[](std::size_t i) //copie modifiable : reference
    {
        return p[i];
    }

    std::size_t size() const
    {
        return s;
    }

    void resize(std::size_t i )
    {
        if(i>s)
        {
            float * tp = new float[i];
            for(std::size_t j = 0; j<s; j++)
            {
                tp[j] = p[j];
            }
            delete [] p;
            p = tp;
            s = i;
        }
        else if (i < s)
        {
            float * tp = new float [i];
            for(std::size_t j = 0; j<i; j++)
            {
                tp[j] = p[j];
            }
            delete [] p;
            p = tp;
            s = i;
        }
    }
};

std::ostream &operator<<(std::ostream & out, vecf const & v)
    {
        for(std::size_t i=0;i<v.size();i++){
            out << v[i] << " ";
        }
        return out;
    }

int main()
{
    vecf v0(10);
    vecf v1(10);

    v0 = v1;

    std::cout << v1 << std::endl;
    std::cout << v1 [3] << std::endl;
    std::cout << v1.size() << std::endl;

    v1[2] = 11.0f;
    std::cout << v1 << std::endl;
    v1.resize(50);
    std::cout << v1 << std::endl;

    return 0;
}
