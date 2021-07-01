# python3

import sys


class Solver:
    def __init__(self, s):
        self.s = s

        #large primes
        self.m1 = 10**9 + 7
        self.m2 = 10**9 + 9

        #random multiplier between 1 and 10**9 + 9, fixing it at 99 for simplicity
        self.x = 99

        #Precompute values
        self.h1 = [0]
        self.h2 = [0]
        for i in range(1, len(s)+1):
            c = s[i-1]
            self.h1.append((self.x * self.h1[i-1] + ord(c)) % self.m1)
            if self.h1[i] < 0: self.h1[i] = (self.h1[i] + self.m1) % self.m1
            self.h2.append((self.x * self.h2[i-1] + ord(c)) % self.m2)
            if self.h2[i] < 0: self.h2[i] = (self.h2[i] + self.m2) % self.m2
    
    def ask(self, a, b, l):


        h1a = self.h1[a+l] - pow(self.x,l,self.m1) * self.h1[a]
        if h1a < 0: h1a = (h1a + self.m1) % self.m1 
        h1b = self.h1[b+l] - pow(self.x,l,self.m1) * self.h1[b]
        if h1b < 0: h1b = (h1b + self.m1) % self.m1
        if h1a != h1b: return False


        h2a = self.h2[a+l] - pow(self.x,l,self.m2) * self.h2[a]
        if h2a < 0: h2a = (h2a + self.m2) % self.m2
        h2b = self.h2[b+l] - pow(self.x,l,self.m2) * self.h2[b]
        if h2b < 0: h2b = (h2b + self.m2) % self.m2
        return h2a == h2b
        

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
