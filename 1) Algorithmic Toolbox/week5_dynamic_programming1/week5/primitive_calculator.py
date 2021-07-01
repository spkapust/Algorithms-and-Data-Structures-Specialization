# Uses python3
import sys
import math

def optimal_sequence(n):
    dp = [None] * (n+1)
    dp[1:4] = [0,1,1]
    for i in range(4,n+1):
        a = dp[i-1]
        b = dp[i//2] if i%2 == 0 else math.inf
        c = dp[i//3] if i%3 == 0 else math.inf
        dp[i] = min(a,b,c) + 1
        

    sequence = []
    while n > 1:
        sequence.append(n)
        a = dp[n-1]
        b = dp[n//2] if n%2 == 0 else math.inf
        c = dp[n//3] if n%3 == 0 else math.inf
        m = min(a,b,c)
        if n % 3 == 0 and dp[n//3] == m:
            n = n // 3
        elif n % 2 == 0 and dp[n//2] == m:
            n = n // 2
        else:
            n = n - 1
    sequence.append(1)
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
