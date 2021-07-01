# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    pisano = "011235831459437077415617853819099875279651673033695493257291"
    pisanopartials = []
    pisanopartials.append(0)
    for i in range(1, len(pisano)):
        pisanopartials.append((pisanopartials[i-1] + int(pisano[i])) % 10)
    return pisanopartials[n%60]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
