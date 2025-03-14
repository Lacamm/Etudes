# include <iostream>
# include <stdlib.h>  // drand48

# include <assert.h>

# undef NDEBUG

# include "matrix.hpp"

using namespace std ;


Matrix :: Matrix() {
  this->line_nbr = 0;
  this->column_nbr = 0;
}

Matrix :: Matrix ( unsigned int const _line_nbr , unsigned int const _column_nbr ) {
  this->line_nbr = _line_nbr;
  this->column_nbr = _column_nbr;
  this->element = new float[_line_nbr*_column_nbr];
}

Matrix :: Matrix ( Matrix const & m ) {
  this->line_nbr = m.line_nbr;
  this->column_nbr = m.column_nbr;
  this->element = new float[m.line_nbr* m.column_nbr];

  for (unsigned int i=0; i<m.line_nbr; i++){
    for (unsigned int j=0; j<m.column_nbr; j++){
      this->element[i*column_nbr+j] = m.element[i*column_nbr+j];
    }
  }
}

Matrix :: ~ Matrix () {
  delete [] element ; // works with NULL
}


void Matrix :: init_alea () {
  for ( unsigned int i = 0 ; i < line_nbr*column_nbr ; i++ ) {
    element[ i ] = drand48 () ;
  }
}

void Matrix :: init ( float const * coefficients ) {
  for ( unsigned int i = 0 ; i < line_nbr*column_nbr ; i++ ) {
    element[ i ] = coefficients[ i ] ;
  }
}

void Matrix :: set_identity () {
}

std :: ostream & operator << ( std :: ostream & ost ,Matrix const & m ) {
  for (unsigned int i=0; i<m.line_nbr; i++){
    for (unsigned int j=0; j<m.column_nbr; j++){
      ost << m(i,j) << "  ";
    }
    ost << endl;
  }
  ost << endl;
  return ost;
}

Matrix & Matrix :: operator = ( Matrix const & m ) {
  this->line_nbr = m.line_nbr;
  this->column_nbr = m.column_nbr;
  this->element = new float[m.line_nbr* m.column_nbr];

  for (unsigned int i=0; i<m.line_nbr; i++){
    for (unsigned int j=0; j<m.column_nbr; j++){
      this->element[i*column_nbr+j] = m.element[i*column_nbr+j];
    }
  }
  return (*this);
}

Matrix Matrix :: operator + ( Matrix const & m ) const {
  if (this->line_nbr == m.line_nbr && this->column_nbr == m.column_nbr){
    Matrix res (m.line_nbr, m.column_nbr);
    for (unsigned int i=0; i<m.line_nbr; i++){
      for (unsigned int j=0; j<m.column_nbr; j++){
        res(i,j) = m.element[i*column_nbr+j]+this->element[i*column_nbr+j];
      }
    }
    return res;
  }
  return m;
}

Matrix Matrix :: operator - ( Matrix const & m ) const {
  if (this->line_nbr == m.line_nbr && this->column_nbr == m.column_nbr){
    Matrix res (m.line_nbr, m.column_nbr);
    for (unsigned int i=0; i<m.line_nbr; i++){
      for (unsigned int j=0; j<m.column_nbr; j++){
        res(i,j) = m.element[i*column_nbr+j]-this->element[i*column_nbr+j];
      }
    }
    return res;
  }
  return m;
}

Matrix Matrix :: operator * ( Matrix const & m ) const {
  if ((this->line_nbr == m.line_nbr && this->column_nbr == m.column_nbr) ||
      (this->line_nbr == m.column_nbr && this->column_nbr == m.line_nbr) ){
    Matrix res (max(m.line_nbr, this->line_nbr), max(m.column_nbr, this->column_nbr));
    for (unsigned int i=0; i<max(m.line_nbr, this->line_nbr); i++){
      for (unsigned int j=0; j<max(m.column_nbr, this->column_nbr); j++){ //faire le cumul
        res(i,j) = m.element[i*column_nbr+j]*this->element[i*column_nbr+j];
      }
    }
    return res;
  }
  return m;
}

Vector Matrix :: operator * ( Vector const & v ) const {
  Vector res (this->line_nbr);
  for (unsigned int i=0; i<this->line_nbr; i++){
    float tmp = 0;
      for (unsigned int j=0; j<v.get_size(); j++){
        tmp += (*this)(i,j)*v[j];
      }
      res[i] = tmp;
    }
    return res;
}

Matrix Matrix :: operator * ( const float a ) const {
}


Matrix operator * ( float const a ,Matrix const & m ) {
  return m * a ;
}


Matrix & Matrix :: operator += ( Matrix const & m ) {
}


Matrix & Matrix :: operator *= ( Matrix const & m ) {
}


bool Matrix :: operator == ( Matrix const & m ) const {
  return false ;
}


Vector Matrix :: extract_ligne ( unsigned int const l ,
				 unsigned int const c1 ,
				 unsigned int const c2 ) const {
  return * ( Vector * ) NULL ;
}


Vector Matrix :: extract_col ( unsigned int const l1 ,
			       unsigned int const l2 ,
			       unsigned int const c ) const {
  return * ( Vector * ) NULL ;
}


Matrix Matrix :: extract_triangular_lower_diag_one () const {
  return * ( Matrix * ) NULL ;
}


Matrix Matrix :: extract_triangular_upper_diag () const {
  return * ( Matrix * ) NULL ;
}


Matrix Matrix :: extract_diagonal () const {
  return * ( Matrix * ) NULL ;
}
