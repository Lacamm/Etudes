#include <mesh.hpp>

#include <iostream>
#include <fstream>
#include <algorithm>
#include <numeric>


mesh load( std::string const & filename )
{
  std::ifstream ifs( filename );

  std::string off;

  unsigned int nbvertices;
  unsigned int nbtriangles;
  unsigned int tmp;

  ifs >> off;
  ifs >> nbvertices;
  ifs >> nbtriangles;
  ifs >> tmp;

  std::cout << off << ' ' << nbvertices << ' ' << nbtriangles << std::endl;
  
  std::vector< vec3< float > > vertices( nbvertices );
  std::vector< vec3< unsigned int > > indices( nbtriangles );
  std::vector< vec3< float > > normals( nbvertices );

  /**
   * generate ou copy (avec istream_iterator)
   */

  // auto lambda = [&ifs](std::generate()){
  //   float x,y,z;
  //   ifs >> x;
  //   ifs >> y;
  //   ifs >> z;
  //   return {x,y,z};
  // };


  for( auto & v: vertices )
  {
    ifs >> v[ 0 ];
    ifs >> v[ 1 ];
    ifs >> v[ 2 ];
  }

  vec3< float > vmin, vmax;
  vec3< float > barycentre;
  
  vmin = vmax = vertices[ 0 ];

  /**
   * for_each ou accumulate.
   */

  std::for_each(vertices.begin(), vertices.end(), [& barycentre, & vmin, & vmax](vec3<auto> v){
  barycentre += v; vmin = min(vmin, v); vmax = max(vmax, v);});

  // for( std::size_t i = 1 ; i < vertices.size() ; ++i )
  // {
  //   vmin = min( vmin, vertices[ i ] );
  //   vmax = max( vmax, vertices[ i ] );
  //   barycentre += vertices[ i ];
  // }

  
  /**
   * generate.
   */

  //std::generate(vertices.begin(), vertices.end(), [&ifs]()
  //{ ifs >> tmp, ifs >> i[ 0 ], ifs >> i[ 1 ] ifs >> i[ 2 ]}
  //);

  for( auto & i: indices )
  {
    ifs >> tmp;
    ifs >> i[ 0 ];
    ifs >> i[ 1 ];
    ifs >> i[ 2 ];
  }


  /**
   * for_each
   */

  std::for_each(indices.begin(), indices.end(),
    [& vertices, & normals](auto i){
      auto v0 = vertices[i[0]];
      auto v1 = vertices[i[1]];
      auto v2 = vertices[i[2]];
      auto n = normalize( cross (v1-v0, v2-v0));
      normals[i[0]] +=n;
      normals[i[1]] +=n;
      normals[i[2]] +=n;
    }
  );


  // for( auto const & i: indices )
  // {
  //   auto & v0 = vertices[ i[ 0 ] ];
  //   auto & v1 = vertices[ i[ 1 ] ];
  //   auto & v2 = vertices[ i[ 2 ] ];

  //   auto n = normalize( cross( v1-v0, v2-v0 ) );

  //   normals[ i[ 0 ] ] += n;
  //   normals[ i[ 1 ] ] += n;
  //   normals[ i[ 2 ] ] += n;
  // }

  /**
   * for_each
   */

  std::for_each(normals.begin(), normals.end(), [](auto & n){n.normalize();});

  // for( auto & n: normals )
  // {
  //   n.normalize();
  // }
  
  return { vertices, indices, normals };
}
