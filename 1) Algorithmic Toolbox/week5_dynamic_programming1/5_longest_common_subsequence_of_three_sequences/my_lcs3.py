#Uses python3

import sys

def lcs3(a, b, c):
    w = len(a) + 1
    h = len(b) + 1
    d = len(c) + 1
    dp = [[[None for x in range(w)] for y in range(h)] for z in range(d)]
   
    #Initialize to 0s
    for i in range(d):
        for j in range(h):
            for k in range(w):
                if i==0 or j==0 or k==0: dp[i][j][k] = 0
   
   
    for i in range(1,d):
        for j in range(1,h):
            for k in range(1,w):
                aa = dp[i-1][j][k]
                bb = dp[i][j-1][k]
                cc = dp[i][j][k-1]
                dd = dp[i-1][j-1][k-1] + 1 if a[k-1] == b[j-1] == c[i-1] else 0
                dp[i][j][k] = max(aa,bb,cc,dd)
    return dp[d-1][h-1][w-1]
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
