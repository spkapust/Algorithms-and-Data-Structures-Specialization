# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    
    #Prime must be greater than len(pattern)*len(text)
    #Per directions, 1 ≤ |𝑃| ≤ |𝑇| ≤ 5 · 10**5. 
    #So 10*11 + 7 is a sufficiently large prime.
    prime = 100000000007

    #Multiplier can be any number in range 1 to prime
    #Making it 1 to simplify 
    multiplier = 1
    
    p_length = len(pattern)
    last_index = len(text) - p_length

    #Get hash of pattern
    hpattern = 0
    for c in pattern:
        hpattern = (hpattern * multiplier + ord(c)) % prime
    
    #Get first hash from text
    htext = 0
    for c in text[0:p_length]:
        htext = (htext * multiplier + ord(c)) % prime

    occurences = []

    if hpattern == htext and pattern == text[0:p_length]:
        occurences.append(0)

    for i in range(1,last_index+1):
        f = text[i-1]
        l = text[i + p_length - 1]
        htext = ((htext*multiplier) + (ord(l)) - (ord(f)*multiplier**p_length)) % prime
        if hpattern == htext and pattern == text[i:i+p_length]:
            occurences.append(i)

    return occurences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

