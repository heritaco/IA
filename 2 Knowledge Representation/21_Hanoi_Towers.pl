% Only one disk:
move(1,Start,End,_):- % move 1 from Start to End
    	write('Move top disk from '),
    	write(Start),
    	write(' pole to '),
    	write(End),
    	write(' pole.'),
    	nl. % Space, new line

% More than 1 disk:
move(N,Start,End,Rest):- 
    	N>1,
    	M is N-1,
    	move(M, Start, Rest, End),
    	move(1, Start, End, _),
    	move(M, Rest, End, Start).

:- initialization(main).

main:- move(4, first, last, middle).