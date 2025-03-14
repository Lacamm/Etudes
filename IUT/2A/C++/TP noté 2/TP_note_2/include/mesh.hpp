#pragma once

#include <vector>
#include <tuple>

#include <vec3.hpp>


using mesh = std::tuple< std::vector< vec3< float > >, std::vector< vec3< unsigned int > >, std::vector< vec3< float > > >;


mesh load( std::string const & filename );
