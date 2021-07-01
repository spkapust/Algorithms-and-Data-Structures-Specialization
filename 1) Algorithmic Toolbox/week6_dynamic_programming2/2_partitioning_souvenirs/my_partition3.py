# Uses python3
import sys
import itertools

def partition3(A):
    if (sum(A) % 3 != 0) or (len(A) < 3): return 0
    W = sum(A) // 3

    rows = len(A) + 1
    cols = W + 1
    dp = [[[0,0] for x in range(cols)] for y in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            currentbest = dp[i-1][j][0] + dp[i-1][j][1]
            if A[i-1] <= j:
                putina = (dp[i-1][j-A[i-1]][0] + A[i-1])+ dp[i-1][j][1]
                putinb = dp[i-1][j][0] + (dp[i-1][j-A[i-1]][1] + A[i-1])
                best = max(currentbest, putina, putinb)
                if best == putina:
                    dp[i][j][0] = dp[i-1][j-A[i-1]][0] + A[i-1]
                    dp[i][j][1] = dp[i-1][j][1]
                elif best == putinb:
                    dp[i][j][0] = dp[i-1][j][0]
                    dp[i][j][1] = dp[i-1][j-A[i-1]][1] + A[i-1]
                else: 
                    dp[i][j]=dp[i-1][j]
            else: 
                dp[i][j]=dp[i-1][j]
    
    if dp[-1][-1] == [W,W]: return 1
    else: return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

