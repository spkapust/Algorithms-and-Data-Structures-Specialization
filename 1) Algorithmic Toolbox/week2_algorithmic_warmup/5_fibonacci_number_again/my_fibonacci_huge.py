# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    p = pisano(m)
    
    previous = 0
    current = 1
    

    if(n%p) == 0: return 0
    if(n%p) == 1: return 1

    for _ in range(n%p-1):
        temp = current
        current = (previous + current) % m
        previous = temp

    return current

def pisano(m):
    previous = 0
    current = 1
    length = 2
    for _ in range(0, m*m):
        temp = current
        current = (previous + current) % m
        previous = temp
        length+=1
        if previous == 0 and current == 1:
            return (length - 2)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
