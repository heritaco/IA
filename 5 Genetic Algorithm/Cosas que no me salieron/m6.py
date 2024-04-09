def find_longest_common_subsequences(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D table to store the lengths of longest common subsequences
    lcs_lengths = [[0] * (n + 1) for _ in range(m + 1)]

    # Compute the lengths of longest common subsequences
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_lengths[i][j] = lcs_lengths[i - 1][j - 1] + 1
            else:
                lcs_lengths[i][j] = max(
                    lcs_lengths[i - 1][j], lcs_lengths[i][j - 1])

    # Find all the longest common subsequences
    subsequences = []
    find_subsequences(str1, str2, m, n, lcs_lengths, "", subsequences)

    # Print the longest common subsequences
    for subsequence in subsequences:
        print(subsequence)


def find_subsequences(str1, str2, i, j, lcs_lengths, current_subsequence, subsequences):
    if i == 0 or j == 0:
        subsequences.append(current_subsequence[::-1])
        return

    if str1[i - 1] == str2[j - 1]:
        find_subsequences(str1, str2, i - 1, j - 1, lcs_lengths,
                          str1[i - 1] + current_subsequence, subsequences)
    elif lcs_lengths[i - 1][j] >= lcs_lengths[i][j - 1]:
        find_subsequences(str1, str2, i - 1, j, lcs_lengths,
                          current_subsequence, subsequences)
    else:
        find_subsequences(str1, str2, i, j - 1, lcs_lengths,
                          current_subsequence, subsequences)


# Test the function
str1 = "agb"
str2 = "gtab"
find_longest_common_subsequences(str1, str2)
