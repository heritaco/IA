"""
Progama que que encuentra la subsecuencia común más larga 
9 Abril 2024
Luis Durán Flores 177406
Heriberto Espino Montelongo 175199
Natalya Patricia Morales De la Vega 177357
"""

def LCS(A, B):
    m = len(A)
    n = len(B)
    
    M = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                M[i][j] = 1 + M[i-1][j-1]
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])

    i = m
    j = n
    lcs = ""
    
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            lcs += A[i-1]
            i -= 1
            j -= 1
        elif M[i-1][j] > M[i][j-1]:
            i -= 1
        else:
            j -= 1

    lcs = lcs[::-1]
    return lcs, len(lcs)

A = ['a', 'g', 'b']
B = ['g', 't', 'a', 'b']
print(LCS(A, B))  

S1 = ['4', '8', '5', '1', '2', '7', '2']
S2 = ['7', '8', '4', '1', '7', '3', '2']
print(LCS(S1, S2))

gato = ['g', 'a', 't', 'o']
atole = ['a', 't', 'o', 'l', 'e']
print(LCS(gato, atole))