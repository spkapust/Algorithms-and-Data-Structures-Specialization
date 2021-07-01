# python3

import sys

def hashvalue(start, stop, l, table, prime, xp):
    value = table[stop] - xp[l] * table[start]
    if value < 0: value = (value + prime) % prime
    return value

def check(i, left, right, err, k, text, pattern):
    #if i == 0: print(left,right)
    #Base cases
    if err > k: return err
    if len(pattern) == 1: 
        if pattern[0] == text[i]: return 0
        else: return 1
    if left == right: return err
    """ if left == right:
        if text[left] != pattern[left-i]:
            return 1
        else: return 0
    if left == right - 1:
        c = 0
        if text[left] != pattern[left-i]: c+=1
        if text[right] != pattern[right-i]: c+=1
        return c  """

    middletext = (left + right) // 2
    middlepattern = middletext - i
    leftpattern = left - i
    rightpattern = right - i
    l = right - left + 1

    #that new new
    leftmismatch=True
    l = middletext - left + 1
    phleft1 = hashvalue(leftpattern, middlepattern + 1, l, hp1, m1, xp1)
    thleft1 = hashvalue(left, middletext + 1, l, ht1, m1, xp1)
    if phleft1 == thleft1:
        phleft2 = hashvalue(leftpattern, middlepattern + 1, l, hp2, m2, xp2)
        thleft2 = hashvalue(left, middletext + 1, l, ht2, m2, xp2)
        if phleft2 == thleft2: leftmismatch = False

    rightmismatch = True
    l = right - middletext 
    phright1 = hashvalue(middlepattern + 1, rightpattern + 1, l, hp1, m1, xp1)
    thright1 = hashvalue(middletext + 1, right + 1, l, ht1, m1, xp1)
    if phright1 == thright1:
        phright2 = hashvalue(middlepattern + 1, rightpattern + 1, l, hp2, m2, xp2)
        thright2 = hashvalue(middletext + 1, right + 1, l, ht2, m2, xp2)
        if phright2 == thright2: rightmismatch = False


    if leftmismatch and rightmismatch: err += 1
    if right-left+1 == len(pattern) and (leftmismatch  or rightmismatch): err += 1
    if err > k: return err
    if leftmismatch: err = check(i, left, middletext, err, k, text, pattern)
    if err > k: return err
    if rightmismatch: err = check(i, middletext+1, right, err, k, text, pattern)
    
    """ #Check left hashes
    l = middletext - left + 1
    phleft1 = hashvalue(leftpattern, middlepattern + 1, l, hp1, m1, xp1)
    thleft1 = hashvalue(left, middletext + 1, l, ht1, m1, xp1)

    errl = 0
    if phleft1 == thleft1:
        phleft2 = hashvalue(leftpattern, middlepattern + 1, l, hp2, m2, xp2)
        thleft2 = hashvalue(left, middletext + 1, l, ht2, m2, xp2)
        if phleft2 != thleft2:
            errl += check(i, left, middletext, err, k, text, pattern)
    else: errl += check(i, left, middletext, err, k, text, pattern)
    

    if err + errl > k: return err + errl
    

    #Check right hashes
    l = right - middletext 
    phright1 = (middlepattern + 1, rightpattern + 1, l, hp1, m1, xp1)
    thright1 = (middletext + 1, right + 1, l, ht1, m1, xp1)

    errr = 0
    if phright1 == thright1:
        phright2 = (middlepattern + 1, rightpattern + 1, l, hp2, m2, xp2)
        thright2 = (middletext + 1, right + 1, l, ht2, m2, xp2)

        if phright2 != thright2:
            errr += check(i, middletext+1, right, err, k, text, pattern)
    else: errr += check(i, middletext+1, right, err, k, text, pattern)


    err = err + errl + errr """
    
    return err

def makeHashTable(s, x, prime):
    ht = list([] for _ in range(len(s)+1))
    ht[0] = 0
    for i in range(1, len(s) + 1):
        c = s[i-1]
        ht[i] = (ht[i - 1] * x + ord(c)) % prime
    return ht

def makePowersTable(x, l, m):
    xp = list([] for _ in range(l))
    for i in range(l):
        xp[i] = pow(x,i,m)
    return xp

def solve(k, text, pattern):

    #large primes
    global m1, m2
    m1 = 10**9 + 7
    m2 = 10**9 + 9

    #random multiplier between 1 and 10**9 + 9, fixing it at 99 for simplicity
    x = 99

    #Precompute hash tables
    global ht1, ht2, hp1, hp2
    ht1 = makeHashTable(text,x,m1)
    ht2 = makeHashTable(text,x,m2)  
    hp1 = makeHashTable(pattern,x,m1)
    hp2 = makeHashTable(pattern,x,m2)

    #precompute xpowers
    global xp1, xp2
    xp1 = makePowersTable(x,len(pattern),m1)
    xp2 = makePowersTable(x,len(pattern),m2)

    occurences = []

    for i in range(len(text)-len(pattern)+1):
        mismatches = check(i, i, i+len(pattern)-1, 0, k, text, pattern)
        if mismatches <= k: occurences.append(i)
    
    return occurences

""" #Test
lines = open("path to test file" , 'r')
correct = open("path to answers file" , 'r')
for line, answer in zip(lines, correct):
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    myans = str(len(ans)) + ' ' +' '.join(str(a) for a in ans)
    myans = myans.strip()
    answer = answer.strip()
    if myans != answer:
        print(line)
        print('myanswer: ', myans)
        print('correct: ', answer)
print('over') """

for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)
