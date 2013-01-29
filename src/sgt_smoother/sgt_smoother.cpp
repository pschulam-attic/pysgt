#include <iostream>
#include "sgt.h"
#include "sgt_smoother.h"

void gt_smooth( int* r, int l1, double* n_r, int l2 )
{
  SGT<int> sgt;
  int j;

  for ( j=0 ; j<l1 ; j++ ) {
    sgt.add( r[j], n_r[j] );
  }

  sgt.analyse();

  pair<SGT<int>::iterator, SGT<int>::iterator> i = sgt.iterate();
  int o;
  double e;
  j = 0;
  for ( ; i.first != i.second ; ++i.first ) {
    o = sgt.obs(i.first);
    e = sgt.estimate(i.first);
    r[j] = o;
    n_r[j] = e;
    j++;
  }
}
