import pprint


def lcs(X, Y):
    """Longest Commons Subsequence"""

    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    pprint.pp(dp)
                
    return dp[m][n]


if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(lcs(X, Y))
