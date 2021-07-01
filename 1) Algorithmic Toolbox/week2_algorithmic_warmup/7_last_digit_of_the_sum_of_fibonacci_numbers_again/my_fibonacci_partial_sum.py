# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    
    pisano = "011235831459437077415617853819099875279651673033695493257291"
    pisanopartials = []
    pisanopartials.append(0)
    for i in range(1, len(pisano)):
        pisanopartials.append((pisanopartials[i-1] + int(pisano[i])) % 10)
    
    
    return ((pisanopartials[to%60] - pisanopartials[(from_-1)%60]) % 10)


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))