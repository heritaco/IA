fullTank.
distance("Mexico","Puebla",132).
travels(X,Y):- distance(X,Y,Z), Z < 500, fullTank.