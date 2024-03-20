factorial(0, 1):- write('factorial of 0 is 1'), nl.

factorial(N, Result):-
    M is N - 1,
    factorial(M, SubResult),
    Result is N * SubResult,
	write('factorial of '), write(N), write(' is '), write(Result), nl.