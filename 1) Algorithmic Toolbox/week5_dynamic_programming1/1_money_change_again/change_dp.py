# Uses python3
import sys

def get_change(m):
    dp = [None] * (m+1)
    dp[0:5] = [0,1,2,1,1]
    #write your code here
    return m // 4

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
