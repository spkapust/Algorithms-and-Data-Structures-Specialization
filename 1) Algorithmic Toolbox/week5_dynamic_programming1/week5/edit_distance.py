# Uses python3
def edit_distance(s, t):
    if s == t: return 0
    w = len(s) + 1
    h = len(t) + 1
    dp = [[None for x in range(w)] for y in range(h)]
    for i in range(w):
        dp[0][i] = i
    for i in range(h):
        dp[i][0] = i
    for i in range(1,h):
        for j in range(1,w):
            a = dp[i-1][j]
            b = dp[i][j-1]
            c = dp[i-1][j-1]
            d = -1 if s[j-1] == t[i-1] else 0
            c = c + d
            dp[i][j] = min(a,b,c) + 1
    return dp[h-1][w-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
