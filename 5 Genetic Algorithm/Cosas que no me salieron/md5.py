def longest_common_subsequence(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]

    # Function to find all LCS and store them in a list
    def find_all_lcs(i, j, seq1, seq2, dp, lcs):
        while i > 0 and j > 0:
            if seq1[i - 1] == seq2[j - 1]:
                lcs.append(seq1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        lcs.reverse()
        return lcs

    lcs_list = []
    for i in range(m + 1):
        for j in range(n + 1):
            if dp[i][j] == lcs_length:
                lcs_list.append(find_all_lcs(i, j, seq1, seq2, dp, []))

    return lcs_length, lcs_list


S1 = ['a', 'g', 'b']
S2 = ['g', 't', 'a', 'b']

longitud, subsecuencias = longest_common_subsequence(S1, S2)

print("La longitud de las subsecuencias común más largas es:", longitud)
for subsecuencia in subsecuencias:
    print("Una subsecuencia común más larga es:", subsecuencia)
