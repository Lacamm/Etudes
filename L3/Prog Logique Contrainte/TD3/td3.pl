/*1*/
affiche([]).
affiche([X|R]) :-write(X),nl,afficher(R).

/*2*/
affiche2([]).
affiche2([X|R]) :-affiche2(R),write(X),nl.

/*3*/
premier1(L,X).
premier1([X|_],X) :-true.

/*5*/
dernier1([X],X).
dernier1([_|Y],Z) :-dernier1(Y,Z).

/*6*/
dernier2([X]) :-write(X), nl.
dernier2([_|L]) :-dernier2(L).

/*7*/
element([X|_],X).
element(X,[_|R]) :-element(X,R).

/*8*/
compte([],0).
compte([_|R],N) :-compte(R,N1),N is N1+1.

/*9*/
somme([],0).
somme([T,Q],S) :-somme(Q,S1), S is S1+T.

/*10 ?*/
nieme1([N],X).
nieme1([Z],Y) :- nieme1(Z,Y).

/*11 ?*/
nieme2([N]).
nieme2(