% consult('007_Cannibals_Missioners.pl').


% 1. State Representation

% state(+MissionersLeft, +CannibalsLeft, +BoatSide)
% MissionersLeft: number of missioners on the left side
% CannibalsLeft: number of cannibals on the left side
% BoatSide: side where the boat is

% 2. Initial State

initial(state(3, 3, left)).
% initial(state(3, 3, right)).
% initial(state(3, 2, left)).
% initial(state(3, 2, right)).
% initial(state(3, 1, left)).

% 3. Final State

final(state(0, 0, _)).

% 4. Movements

% move(+Move, +State, +NewState)

% 4.1. Move 1 missioner from left to right

move(1, state(M, C, left), state(M1, C, right)) :-
    M > 0,
    M1 is M - 1.