#include <iostream>

#include <mesh.hpp>


int main()
{
  auto m0 = load( "models/rabbit.off" );

  for( auto const & x: std::get<2>( m0 ) )
  {
    std::cout << x[ 0 ] << ' ' << x[ 1 ] << ' ' << x[ 2 ] << std::endl;
  }

  return 0;
}
