include "globals.mzn";

var 1..9 : s;
var 0..9 : e;
var 0..9 : n;
var 0..9 : d;
var 1..9 : m;
var 0..9 : o;
var 0..9 : y;
%var 0..9 : r;
var 0..9 : t;

constraint s != 0;
constraint m != 0;
%constraint ((s*1000)+(e*100)+(n*10)+d)+((m*1000)+(o*100)+(r*10)+e) = ((m*10000)+(o*1000)+(n*100)+(e*10)+y);
constraint ((s*1000)+(e*100)+(n*10)+d)+((m*1000)+(o*100)+(s*10)+t) = ((m*10000)+(o*1000)+(n*100)+(e*10)+y);
%constraint alldifferent([s,e,n,d,m,o,r,y]);
constraint alldifferent([s,e,n,d,m,o,t,y]);

solve maximize m*10000+o*1000+n*100+e*10+y;
