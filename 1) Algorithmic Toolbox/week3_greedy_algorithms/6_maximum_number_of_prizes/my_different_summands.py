# Uses python3
import sys

def optimal_summands(n):
    summands = []
    

    nums = 1
    while ( nums*(nums+1) <= 2*n ):
        nums+=1
    nums -= 1

    if nums == 1:
        summands.append(n)
    else:
        total = 0
        for i in range(1,nums):
            summands.append(i)
            total += i
        summands.append(n-total)
    
    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
