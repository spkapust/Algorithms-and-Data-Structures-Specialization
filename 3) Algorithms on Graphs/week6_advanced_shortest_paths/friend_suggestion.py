#!/usr/bin/python3

import sys
import heapq

class BiDij:
    def __init__(self, n):
        self.n = n                              # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [dict(), dict()]               # Initialize distances for forward and backward searches
        self.visited = [dict(), dict()]         # visited[v] == True iff v was visited by forward or backward search
        self.prev = [dict(), dict()]
        #self.workset = set()                       # All the nodes visited by forward or backward search
        self.best = self.inf

    def clear(self):
    #Reinitialize the data structures for the next query after the previous query.
        self.d[0].clear()
        self.d[1].clear() 
        self.visited[0].clear()
        self.visited[1].clear()
        self.prev[0].clear()
        self.prev[1].clear()
        self.best = self.inf

    def visit(self, q, side, v, dist, n):
    #Try to relax the distance to node v from direction side by value dist.
        if self.d[side].get(v, self.inf) > dist:
            self.d[side][v] = dist
            heapq.heappush(q[side], (dist, v))
            self.prev[side][v] = n
            if self.d[0].get(v, self.inf) + self.d[1].get(v, self.inf) < self.best:
                self.best = self.d[0][v] + self.d[1][v] 
        return

    def query(self, adj, cost, s, t):
        if s == t: return 0
        self.clear()
        q = [[], []]
        
        self.visit(q, 0, s, 0, s)
        self.visit(q, 1, t, 0, t)
        d1 = 0
        d2 = 0
        
        while(len(q[0]) and len(q[1])):

            for i in range(2):
                d1, v = heapq.heappop(q[i])
                
                if d1 + d2 >= self.best:
                    return self.best

                if not self.visited[i].get(v, False):
                    for idx, n in enumerate(adj[i][v]):
                        dist = cost[i][v][idx] + self.d[i][v]
                        self.visit(q, i, n, dist, v)
                    self.visited[i][v] = True
                    if self.visited[(i+1)%2].get(v, False) == True:
                        return self.best
                
                d2 = d1
        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))
