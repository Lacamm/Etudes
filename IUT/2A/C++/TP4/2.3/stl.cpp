#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <cmath>
#include <iterator>


template < typename T >
std::ostream & operator<<( std::ostream & out, std::vector< T > const & v )
{
  for( auto x: v )
  {
    out << x << std::endl;
  }
  return out;
}



template < typename T, std::size_t N >
std::ostream & operator<<( std::ostream & out, std::array< T, N > const & v )
{
  for( auto x: v )
  {
    out << x << std::endl;
  }
  return out;
}

class Banane
{
  float a;
  
  using value_type = float;
};

std::ostream & operator<<( std::ostream & out, Banane const & b )
{
  out << "banane";
  return out;
}

/*
template < typename T0, typename T1>
struct pair
{
  T0 first;
  T1 second;
};
*/


struct acc
{
  float tmp;
  acc(): tmp(0.0f) {}

  void operator()( float f )
  {
    tmp += f*f;
  }
};

void display( float f )
{
  std::cout << f << std::endl;
}

int main()
{
  std::vector< float > v( 10 );
  std::vector< float > v0;

  std::generate( v.begin(), v.end(), []() { return (std::rand()%10)/10.0f; } );

  std::cout << v << std::endl;

  float tmp = 0.0f;
  float scale = 2.0f;

  auto lambda = []() { return 5; };

  std::cout << lambda() << std::endl;
  
  //std::for_each( v.begin(), v.end(), display );
  //std::for_each( v.begin(), v.end(), []( float f ) { std::cout << f << std::endl; } );

  std::copy( v.begin(), v.end(), std::ostream_iterator< float >( std::cout, " ") );
  std::cout << std::endl;
  
  std::for_each( v.begin(), v.end(), [&tmp,scale]( float f ) { tmp += f*f*scale; } );
  
  std::cout << std::sqrt( tmp ) << std::endl;

  std::sort(begin(v), end(v), [](float a, float b) {return a > b;});
  
  std::cout << v << std::endl;

  std::transform( cbegin(v), cend(v), std::back_inserter(v0), [](float f ){return f*=2 ;} );


  /*
  acc a0;
  a0 = std::for_each( v.begin(), v.end(), a0 );

  std::cout << std::sqrt( a0.tmp ) << std::endl;
  */
  
  return 0;
}
