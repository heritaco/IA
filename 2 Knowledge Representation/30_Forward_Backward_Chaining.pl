    % consult('016_Forward_Backward_Chaining.pl').

    come(aguila, serpiente).
    come(serpiente, raton).
    come(raton, grillo).
    come(grillo, hierba).

    come(tiburon, pez).
    come(pez, camaron).
    come(camaron, plancton).

    come(X, Y) :- come(X, Z), come(Z, Y). % regla recursiva

    % forward chaining:
    % aguila -> serpiente
    % serpiente -> raton
    % _________________________
    % aguila -> raton


    % backward chaining:
    % aguila ->  raton ??
    % _________________________
    % aguila -> serpiente
    % serpiente -> raton    