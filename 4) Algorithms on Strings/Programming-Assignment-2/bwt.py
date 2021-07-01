# python3
import sys

def BWT(text):
    rotations = []
    for i, _ in enumerate(text):
        r = text[i:] + text[:i]
        rotations.append(r)
    rotations.sort()
    char_list = []
    for r in rotations:
        char_list.append(r[-1])
    return ''.join(char_list)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))