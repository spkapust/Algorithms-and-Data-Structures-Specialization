#Uses python3

import sys

def lcs2(a, b):
    w = len(a) + 1
    h = len(b) + 1
    dp = [[None for x in range(w)] for y in range(h)]
    
    #Initialize to 0s
    for i in range(w):
        dp[0][i] = 0
    for i in range(h):
        dp[i][0] = 0
    
    for i in range(1,h):
        for j in range(1,w):
            c = dp[i-1][j]
            d = dp[i][j-1]
            e = dp[i-1][j-1] + 1 if a[j-1] == b[i-1] else 0
            dp[i][j] = max(c,d,e)
    return dp[h-1][w-1]
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
