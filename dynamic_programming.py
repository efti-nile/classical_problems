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


def test_lcs():
    print("Longest Commons Subsequence:")
    X = "AGGTAB"
    Y = "AGXTXAYB"
    print(lcs(X, Y))


def knapsack(weights, values, capacity):
    """Knapsack Problem"""

    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    pprint.pp(dp)
                
    return dp[n][capacity]


def test_knapsack():
    print("Knapsack:")
    weights = [1, 2, 3, 4]
    values = [1, 4, 4, 5]
    capacity = 5
    print(knapsack(weights, values, capacity))


if __name__ == '__main__':
    test_lcs()
    test_knapsack()
