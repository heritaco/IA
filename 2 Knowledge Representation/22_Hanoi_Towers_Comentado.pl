% Esta es una solución al problema de la Torre de Hanoi.

% El predicado move define cómo mover N discos de un poste a otro.
% Toma cuatro argumentos: el número de discos a mover, el poste de inicio, el poste final y el poste restante.

% Caso base: si solo hay un disco para mover (N es 1), simplemente lo movemos del poste de inicio al poste final.
move(1,Start,End,_):- 
    write('Mover el disco superior de '),  % Imprimir el inicio del mensaje de movimiento
    write(Start),  % Imprimir el poste de inicio
    write(' poste a '),  % Imprimir el medio del mensaje de movimiento
    write(End),  % Imprimir el poste final
    write(' poste.'),  % Imprimir el final del mensaje de movimiento
    nl.  % Imprimir un carácter de nueva línea

% Caso recursivo: si hay mas de un disco para mover (N es mayor que 1), necesitamos hacer varios movimientos.
move(N,Start,End,Rest):- 
    N>1,  % Comprobar si N es mayor que 1
    M is N-1,  % Calcular M como N menos 1
    move(M, Start, Rest, End),  % Mover M discos del poste de inicio al poste restante, utilizando el poste final como almacenamiento temporal
    move(1, Start, End, _),  % Mover el disco mas grande del poste de inicio al poste final
    move(M, Rest, End, Start).  % Mover M discos del poste restante al poste final, utilizando el poste de inicio como almacenamiento temporal

% El predicado main se llama automáticamente cuando comienza el programa.
:- initialization(main).

% El predicado main resuelve el problema de la Torre de Hanoi para 4 discos.
main:- move(4, first, last, middle).