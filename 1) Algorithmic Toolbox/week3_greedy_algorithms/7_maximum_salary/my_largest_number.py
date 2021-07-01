#Uses python3

import sys

def isGreaterOrEqual(digi, maxdigi):
    a = str(digi) + str(maxdigi)
    b = str(maxdigi) + str(digi)
    if int(a) >= int(b): return True
    return False


def largest_number(a):
    #write your code here
    res = ""
    while len(a) > 0:
        maxd = 0
        for x in a:
            if isGreaterOrEqual(x, maxd):
                maxd = x
        res+=maxd    
        a.remove(maxd)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
