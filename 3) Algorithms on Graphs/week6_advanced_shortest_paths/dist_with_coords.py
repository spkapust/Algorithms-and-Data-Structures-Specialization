#!/usr/bin/python3

import sys
import math
import heapq

class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion        
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n*10**6
        self.d = [self.inf]*n
        self.visited = [False]*n
        self.workset = set()
        self.potentials = {}
        # Coordinates of the nodes
        self.x = x
        self.y = y

    # See the explanation of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.workset:
            self.d[v] = self.inf
            self.visited[v] = False
        self.potentials.clear()
        self.workset.clear()

    # See the explanation of this method in the starter for friend_suggestion
    def visit(self, q, p, v, dist, measure):
        if self.d[p] + dist + measure < self.d[v]:
            self.d[v] = self.d[p] + dist + measure
            heapq.heappush(q, (self.d[v], v))
        pass

    def get_potential(self, v, t):
        if v not in self.potentials:
            dx2 = (self.x[v] - self.x[t])**2
            dy2 = (self.y[v] - self.y[t])**2
            self.potentials[v] = math.sqrt(dx2 + dy2)
        return self.potentials[v]

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        if s == t: return 0
        
        self.clear()
        q = []
        self.d[s] = 0
        self.workset.add(s)
        q.append((0,s))
        while (len(q)):
            v = heapq.heappop(q)[1]
            if v == t:
                return round(self.d[t] + self.get_potential(s, t))
            if self.visited[v] == False:
                for idx, n in enumerate(adj[v]):
                    dist = cost[v][idx]
                    measure = self.get_potential(n, t) - self.get_potential(v, t)
                    self.visit(q,v,n,dist,measure)
                    self.workset.add(n)
                self.visited[v] = True
        
        return -1

def readl():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    n,m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u,v,c = readl()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)

    # qs = open('c:/Users/skapust/Desktop/Courses & Books/Algorithms on Graphs/week6_advanced_shortest_paths/dist_with_coords/tests/03.q', 'r').readlines()
    # answers = open('c:/Users/skapust/Desktop/Courses & Books/Algorithms on Graphs/week6_advanced_shortest_paths/dist_with_coords/tests/03.a', 'r').readlines()
    # for i in range(len(qs)):
    #     s, t = map(int, qs[i].split())
    #     b = astar.query(s-1, t-1)
    #     a = int(answers[i])

    #     if a != round(b):
    #         print(s,t)
    #         print(a,b)
    #         print("BROKEN")
    #         #break

    
    for i in range(t):
        s, t = readl()
        print(astar.query(s-1, t-1))
        
