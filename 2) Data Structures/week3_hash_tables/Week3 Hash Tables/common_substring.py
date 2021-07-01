# python3

import sys
import random
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def solve(s, t):
    maxlength = min(len(s), len(t))
    
    #large primes
    m1 = 10**9 + 7
    m2 = 10**9 + 9

    #random multiplier between 1 and 10**9 + 9, fixing it at 99 for simplicity
    x = 99

    #Precompute hash tables
    hs1 = [0]
    hs2 = [0]
    for i in range(1, len(s)+1):
            c = s[i-1]
            hs1.append((x * hs1[i-1] + ord(c)) % m1)
            if hs1[i] < 0: hs1[i] = (hs1[i] + m1) % m1
            hs2.append((x * hs2[i-1] + ord(c)) % m2)
            if hs2[i] < 0: hs2[i] = (hs2[i] + m2) % m2
    
    ht1 = [0]
    ht2 = [0]
    for i in range(1, len(t)+1):
            c = t[i-1]
            ht1.append((x * ht1[i-1] + ord(c)) % m1)
            if ht1[i] < 0: ht1[i] = (ht1[i] + m1) % m1
            ht2.append((x * ht2[i-1] + ord(c)) % m2)
            if ht2[i] < 0: ht2[i] = (ht2[i] + m2) % m2

    #setup start for binary search through lengths
    low = 1
    high = maxlength
    k = (low+high)//2
    prevk = 0 
    ans = Answer(0, 0, 0)
    
    while(k != prevk):
        matchedk = False
        d1 = {}
        d2 = {}

        for i in range(0,len(s)+1-k):
            s1 = hs1[i+k] - pow(x,k,m1) * hs1[i]
            if s1 < 0: s1 = (s1 + m1) % m1
            s2 = hs2[i+k] - pow(x,k,m2) * hs2[i]
            if s2 < 0: s2 = (s2 + m2) % m2
            d1[s1] = i
            d2[s2] = i
            
        for j in range(0,len(t)+1-k):
            t1 = ht1[j+k] - pow(x,k,m1) * ht1[j]
            if t1 < 0: t1 = (t1 + m1) % m1
            if t1 not in d1: continue
            else: 
                t2 = ht2[j+k] - pow(x,k,m2) * ht2[j]
                if t2 < 0: t2 = (t2 + m2) % m2
                if t2 in d2:
                    ans = Answer(d2[t2], j, k)
                    matchedk = True
                    break

        #fix binary search
        if matchedk: low = min(k + 1, high)
        else: high = max(low, k - 1)
        prevk = k
        k = (low+high)//2
        

    """ #run it back because, we still need to check that final K value
    matchedk = False
    d1 = {}
    d2 = {}
    for i in range(0,len(s)+1-k):
        s1 = hs1[i+k] - pow(x,k,m1) * hs1[i]
        if s1 < 0: s1 = (s1 + m1) % m1
        s2 = hs2[i+k] - pow(x,k,m2) * hs2[i]
        if s2 < 0: s2 = (s2 + m2) % m2
        d1[s1] = i
        d2[s2] = i
        
    for j in range(0,len(t)+1-k):
        t1 = ht1[j+k] - pow(x,k,m1) * ht1[j]
        if t1 < 0: t1 = (t1 + m1) % m1
        if t1 not in d1: continue
        else: 
            t2 = ht2[j+k] - pow(x,k,m2) * ht2[j]
            if t2 < 0: t2 = (t2 + m2) % m2
            if t2 in d2:
                ans = Answer(d2[t2], j, k)
                break """

    return ans

def naive_solve(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans

#stress test
""" while(True):
    lnth = random.randint(1,1000)
    leter = "abzeb"
    firstr = ''.join((random.choice(leter) for i in range(lnth)))
    secstr = ''.join((random.choice(leter) for i in range(lnth)))
    print(firstr, secstr)
    ans = solve(firstr,secstr)
    print("finished ya solve")
    ans2 = naive_solve(firstr,secstr)
    if ans.len != ans2.len:
        print(False)
        print(firstr,secstr)
        print('my solution is ',ans)
        print('naive solution is ',ans2)
        break """

for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
