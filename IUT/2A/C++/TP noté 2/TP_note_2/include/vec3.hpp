#pragma once


#include <array>
#include <cmath>


template < typename T >
class vec3
{
private:
  std::array< T, 3 > v_;

public:
  vec3(): v_{ {} } {}

  vec3( T x, T y, T z ): v_{ x, y, z } {}

  T operator[]( std::size_t i ) const 
  {
    return v_[ i ];
  }
  T & operator[]( std::size_t i )
  {
    return v_[ i ];
  }

  /**
   * Il manque un opérateur ici.
   */

  vec3<T> & operator+=(vec3<T> const & v0)
  {
    v_[0]+=v0[0];
    v_[1]+=v0[1];
    v_[2]+=v0[2];
    return *this;
  }

  
  /**
   * Il manque la méthode normalize ici.
   */

  void normalize()
  {
    T inv_norm = 1.0f/std::sqrt(v_[0]*v_[0]+v_[1]*v_[1]+v_[2]*v_[2]);

    v_[0] *= inv_norm;
    v_[1] *= inv_norm;
    v_[2] *= inv_norm;
  }
  
};

template < typename T >
vec3< T > operator-( vec3< T > const & v0, vec3< T > const & v1 )
{
  return { v0[ 0 ] - v1[ 0 ], v0[ 1 ] - v1[ 1 ], v0[ 2 ] - v1[ 2 ] };
}

/**
 * Il manque un opérateur ici.
 */


template < typename T >
vec3< T > cross( vec3< T > const & v0, vec3< T > const & v1 )
{
  return {
    v0[ 1 ] * v1[ 2 ] - v0[ 2 ] * v1[ 1 ],
    v0[ 2 ] * v1[ 0 ] - v0[ 0 ] * v1[ 2 ],
    v0[ 0 ] * v1[ 1 ] - v0[ 1 ] * v1[ 0 ]
  };
}

template < typename T>
vec3<T> normalize(vec3<T> const v)
{
  T inv_norm = 1.0f/std::sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]);

  return
  {
    v[0] * inv_norm,
    v[1] * inv_norm,
    v[2] * inv_norm,
  };
}

/**
 * Il manque les fonctions min et max ici !
 */

template <typename T>
T min( T v0, T v1 )
{
  return{ std::min(v0[0], v0[1]), std::min(v0[1], v1[1]), std::min(v0[2], v1[2]) };
}

template <typename T>
T max( T v0, T v1 )
{
  return{ std::max(v0[0], v0[1]), std::max(v0[1], v1[1]), std::max(v0[2], v1[2]) };
}