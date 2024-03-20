% consult('Water_Jug_Problem').pl

    /*
    We have a 3-liter jug, a 5-liter jug, and an unlimited supply of water. 
    Goal: to get exactly 1 liter of water into either jug. 
    Either jug can be emptied or filled, or poured into the other. 
    A state in this problem could be represented with just a pair of numbers, 
    the first representing the number of liters of water in the 5-liter (large) jug, 
    and the second representing the number of liters of water in the 3-liter (small) jug.
    */

% facts
initial_state([0,0]).
final_state([0,1];[1,0]). % final state is either [0,1] or [1,0]

% rules
fill_5([_,X],[5,X]). % fill the 5 liter jug
fill_3([X,_],[X,3]). % fill the 3 liter jug
empty_5([_,X],[0,X]). % empty the 5 liter jug
empty_3([X,_],[X,0]). % empty the 3 liter jug 
fill_3_into_5([X,Y],[X2,Y2]) :- X2 is X + Y,  X2 =< 5, Y2 is 5 - X, X >= 0, Y >= 0, X2 >= 0, Y2 >= 0. % pour water from the 3 liter jug into the 5 liter jug until its capacity is reached
fill_5_into_3([X,Y],[X2,Y2]) :- Y2 is X + Y,  Y2 =< 3, X2 is 3 - Y, X >= 0, Y >= 0, X2 >= 0, Y2 >= 0. % pour water from the 5 liter jug into the 3 liter jug until its capacity is reached


% Define a helper predicate to check if a state has been visited
visited(State, [State|_]).
visited(State, [_|Rest]) :- visited(State, Rest).


action(State, NextState) :-
    fill_5(State, NextState);
    fill_3(State, NextState);
    empty_5(State, NextState);
    empty_3(State, NextState);
    fill_3_into_5(State, NextState);
    fill_5_into_3(State, NextState).


% Correct the solve predicate
solve(State, [State]) :- final_state(State).
solve(State, Path) :-
    action(State, NextState),
    not(visited(NextState, Path)),
    solve(NextState, Rest),
    Path = [State|Rest].