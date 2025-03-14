# include <stdlib.h>
# include <assert.h>
# include "vector.hpp"

using namespace std ;

Vector :: Vector ( ) {
  this->size = 0;
}

Vector :: Vector ( unsigned int const _size ) {
  this->size = _size;
  this->element = new float[_size];
}

Vector :: Vector ( const Vector & v ) {
  this->size = v.size;
  this->element = new float[v.size];
  for( unsigned int i=0; i<v.size; i++){
    this->element[i] = v.element[i];
  }
}

Vector :: ~Vector () {}

void Vector :: init_alea () {
  for ( unsigned int i = 0 ; i < size ; i++ ) {
    element[ i ] = drand48 () ;
  }
}

float & Vector :: operator [] ( unsigned int const i ) {
  return this->element[i];
}

float const & Vector :: operator [] ( unsigned int const i ) const {
  return this->element[i];
}

std :: ostream & operator << ( std :: ostream& ost ,Vector const & v ) {
  for (unsigned int i=0; i<v.size; i++){
    ost << v[i] << ", ";
  }
  ost << endl;
  return ost ;
}

Vector & Vector :: operator = ( Vector const & v ) {
  this->size = v.size;
  this->element = new float[v.size];
  for( unsigned int i=0; i<v.size; i++){
    this->element[i] = v.element[i];
  }
  return ( * this ) ;
}

Vector Vector :: operator + ( Vector const & v ) const {
  if (this->size == v.size){
    Vector res (v.size);
    for (unsigned int i=0; i<v.size; i++){
      res [i] = v.element[i]+this->element[i];
    }
    return res;
  }
  return v;
}

Vector Vector :: operator - ( Vector const & v ) const {
  if (this->size == v.size){
    Vector res (v.size);
    for (unsigned int i=0; i<v.size; i++){
      res [i] = v.element[i]-this->element[i];
    }
    return res;
  }
  return v;
}

Vector Vector :: operator * ( float const a ) const {
  Vector res (this->size);
  for (unsigned int i=0; i<this->size; i++){
    res [i] = a*(this->element[i]);
  }
  return res;
}

float Vector :: operator | ( Vector const & v ) const {
  if (this->size == v.size){
    float res;
    for (unsigned int i=0; i<v.size; i++){
      res += v.element[i]*this->element[i];
    }
    return res;
  }
  return 0;
}

bool Vector :: operator == ( Vector const & v ) const {
  if (this->size == v.size){
    for(unsigned int i=0; i<this->size; i++){
      if(this->element[i]!=v.element[i]){
        return false;
      }
    }
    return true;
  }
  return false ;
}

Vector operator * ( float const a , Vector const & v ) {
  Vector res (v.get_size());
  for (unsigned int i=0; i<v.get_size(); i++){
    res[i] = a*v[i];
  }
  return res;
}
