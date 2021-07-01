# Uses python3
import sys

def optimal_weight(W, w):
    cols = W + 1
    rows = len(w) + 1
    dp = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(1,rows):
        for j in range(1,cols):
            a = dp[i-1][j]
            if w[i-1] <= j: 
                b = dp[i-1][j-w[i-1]] + w[i-1]
                dp[i][j] = max(a,b)
            else: dp[i][j] = a
    return dp[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
