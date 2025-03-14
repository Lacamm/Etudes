#include <iostream>
#include <array>

template < typename T, std::size_t N, std::size_t M >
class matrix
{
private:
  std::array< T, N*M > data_;

  
public:

  using value_type = T;
  
  matrix(): data_{ {} } {}

  T operator()( std::size_t i, std::size_t j ) const
  {
    return data_[ j*N+i ];
  }
  T & operator()( std::size_t i, std::size_t j )
  {
    return data_[ j*N+i ];
  }
  
};

template < typename T, std::size_t N, std::size_t M >
std::ostream & operator<<( std::ostream & out, matrix< T, N, M > const & m )
{
  for( std::size_t j = 0 ; j < M ; ++j )
  {
    for( std::size_t i = 0 ; i < N ; ++i )
    {
      out << m( i, j ) << '\t';
    }
    out << std::endl;
  }
  
  return out;
}


/**
 * Mulitplication de 2 matrices de même type et de tailles correspondantes.
 */
template < typename T0, std::size_t N, std::size_t X, std::size_t Y >
matrix< T0, Y, X > operator*( matrix< T0, N, X > const & m0, matrix< T0, Y, N > const & m1 )
{
  // Produit de matrices a implanter.
  return {};
}

/**
 * Multiplication de 2 matrices de types différents, mais quel type retour choisir ??? Le type T2 doit être donné explicitement à l'opérateur * cf appel commenté dans le main, ou alors il faut choisir T0 ou T1.
 */
/*
template < typename T0, typename T1, typename T2, std::size_t N, std::size_t X, std::size_t Y >
matrix< T2, Y, X > operator*( matrix< T0, N, X > const & m0, matrix< T1, Y, N > const & m1 )
{
  return {};
}
*/

/**
 * Addition de 2 matrices de même type : type de valeur + taille.
 */
template < typename T, std::size_t N, std::size_t M>
matrix< T, N, M > operator+( matrix< T, N, M > const & m0, matrix< T, N, M > const & m1 )
{
  // Addition à implanter.
  return {};
}



  
int main()
{
  matrix< float, 4, 3 > m0;
  matrix< float, 5, 4 > m1;

  m0( 1, 1 ) = 3.0f;

  std::cout << m0 << std::endl;

  // Appel explicite à l'opérateur * avec les types spécifiés.
  //auto m2 = operator*< float, double, float, 4, 3, 5>(m0, m1);
  auto m2 = m0 * m1;

  std::cout << m2 << std::endl;

  std::cout << sizeof( decltype(m2)::value_type ) << std::endl;
  
  return 0;
}
