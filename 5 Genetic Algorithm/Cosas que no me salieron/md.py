def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]

def plagiarism_detector(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    similarity = lcs(text1, text2)
    similarity_percentage = (similarity / max(len(text1), len(text2))) * 100

    return similarity_percentage

# Usage example
file1 = 'C:\Users\herie\Downloads\Sin titulo.txt'
file2 = 'C:\Users\herie\Downloads\a model trained on one task is reus.txt'
similarity_percentage = plagiarism_detector(file1, file2)
print(f"Similarity percentage: {similarity_percentage}%")