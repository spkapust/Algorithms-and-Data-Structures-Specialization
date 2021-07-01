# Uses python3
import sys

def get_change(m):
    dp = [None] * (m+1)
    dp[0:5] = [0,1,2,1,1]
    for i in range(5, m+1):
        dp[i] = min(dp[i-1], dp[i-3], dp[i-4]) + 1
    return dp[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
