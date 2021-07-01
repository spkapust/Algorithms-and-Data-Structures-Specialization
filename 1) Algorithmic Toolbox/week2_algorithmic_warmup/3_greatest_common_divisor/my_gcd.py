# Uses python3
import sys

def gcd_naive(a, b):
    if a == 0: return b
    if b == 0: return a
    divisor = min(a,b)
    remainder = max(a,b) % divisor
    while remainder > 0:
        temp = remainder
        remainder = divisor % remainder
        divisor = temp
    return divisor


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
