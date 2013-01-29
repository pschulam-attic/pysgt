%module sgt_smoother

%{
  #define SWIG_FILE_WITH_INIT
  #include "sgt_smoother.h"
%}

%include "numpy.i"

%init %{
  import_array();
%}

%apply (int* INPLACE_ARRAY1, int DIM1) {(int *r, int l1)}
%apply (double *INPLACE_ARRAY1, int DIM1) {(double *n_r, int l2)}

%include "sgt_smoother.h"
