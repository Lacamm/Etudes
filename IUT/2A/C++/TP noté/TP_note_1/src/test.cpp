#include <iostream>


/**
 * Step 1.
 */
#include <vec4f.hpp>


/**
 * Steps 2 and 3.
 */
#include <mat4x4f.hpp>
/**
 * Step 4.
 */
//#include <transform.hpp>


int main()
{
  /**
   * Step 1.
   */
  vml::vec4f v0 = { 1.0f, 2.0f, 3.0f, 4.0f };

  std::cout << "v0\n" << v0 << std::endl;

  vml::vec4f v1 = { 1.0f };

  v1[ 2 ] = 7.5f;
  
  std::cout << "v1\n" << v1 << std::endl;

  std::cout << "v1*3.0f\n" << v1 * 3.0f << std::endl;

  std::cout << "v0*v1\n" << v0 * v1 << std::endl;

  v0 += v1;
  
  std::cout << "v0\n" << v0 << std::endl;
  /**
   * Step 2.
   */
  
  vml::mat4x4f m0;

  std::cout << "m0\n" << m0 << std::endl;

  vml::mat4x4f m1;
  m1[ 0 ][ 0 ] = m1[ 1 ][ 1 ] = m1[ 2 ][ 2 ] = m1[ 3 ][ 3 ] = 1.0f;

  std::cout << "m1\n" << m1 << std::endl;
    
  m0[ 0 ] = v0;

  std::cout << "m0\n" << m0 << std::endl;

  m0[ 1 ][ 2 ] = 7.0f;
  
  std::cout << "m0\n" << m0 << std::endl;
  
  /**
   * Step 3.
   */
  
  //auto v2 = m0 * v0;

  //std::cout << "v2\n" << v2 << std::endl;

  //std::cout << "m0 + m1\n" << m0 + m1 << std::endl;

  //std::cout << "m0 * m1*2.0f\n" << m0 * 2.0f*m1 << std::endl;
  
  /**
   * Step 4.
   */
  /*
  vml::vec3f v3 = { 1.0f, 0.0f, 0.0f };

  // rotation along the z axis.
  auto r0 = vml::rotate( M_PI/4.0f, { 0.0f, 0.0f, 1.0f } );

  // rotation of v3.
  std::cout << "r0*v3\n" << r0*v3 << std::endl;

  // rotation + translation of v3.
  std::cout << vml::translate( { 1.0f, 0.0f, 0.0f } )*r0*v3 << std::endl;
  */
  return 0;
}
