parent(tom, bob).
parent(pam, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

% parent (X, ann) -> X=bob
% parent (Y, jim, parent(x,Y)) -> X=bob Y=pat

% rules
% representating:
% for all X and Y: Y is and offspring of X if X is parent of Y
offspring(Y, X):-
    parent(X,Y).

grandparent(X,Z):- % X is the grandparent of Z if:
    parent(X,Y),   % X is parent of Y
    parent(Y,Z).   % Y is parent of Z

% Recursive rule

predecessor(X,Z):-
    parent(X,Y),
    predecessor(Y,Z).

predecessor(X,Z):- % The rule that stopts
    parent(X,Z).
