#!/usr/bin/python3


import sys
#import queue
import itertools
import heapq


# Maximum allowed edge length
maxlen = 2 * 10**6


class DistPreprocessLarge:
    def __init__(self, n, adj, cost):
        # See description of these parameters in the starter for friend_suggestion
        self.n = n
        self.INFINITY = n * maxlen
        self.adj = adj
        self.cost = cost
        self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
        self.visited = [[False] * n, [False]*n]
        self.workset = set()
        self.q = []
        # Levels of nodes for node ordering heuristics
        self.level = [0] * n
        # Positions of nodes in the node ordering
        self.rank = [0] * n
        self.stopping_distances = [0]*n
        # Indication if nodes are contracted or not
        self.contracted = [False]*n

        # Implement preprocessing here
        self.get_stopping_distances()

        for v in range(self.n):
            importance, shortcuts = self.witness_search(v)
            heapq.heappush(self.q, (importance,v))
        
        r = 0
        
        while(len(self.q)):
            v = heapq.heappop(self.q)[1]
            
            if not len(self.q):
                self.rank[v] = r
                continue
            new_importance, shortcuts = self.witness_search(v)
            
            if new_importance <= self.q[0][0]:
                #contract
                self.contracted[v] = True
                self.rank[v] = r
                r += 1
                self.update_levels(v)
                for s in shortcuts:
                    self.add_arc(s[0],s[1],s[2])
            else:
                heapq.heappush(self.q, (new_importance, v))

        return

    def get_stopping_distances(self):
        for v in range(self.n):
            maximum_outgoing_edge = 0
            for idx, _ in enumerate(self.adj[0][v]):
                maximum_outgoing_edge = max(maximum_outgoing_edge, cost[0][v][idx])
            
            maximum_incoming_edge = 0
            for idx, _ in enumerate(self.adj[1][v]):
                maximum_incoming_edge = max(maximum_incoming_edge, cost[1][v][idx])

            minimum_predecessor = self.INFINITY
            for w in self.adj[0][v]:
                for idx, n in enumerate(self.adj[1][w]):
                    if n != v:
                        minimum_predecessor = min(minimum_predecessor, cost[1][w][idx])
            
            stopping_distance = maximum_outgoing_edge + maximum_incoming_edge - minimum_predecessor
            self.stopping_distances[v] = stopping_distance

    def update_levels(self, v):
        l = self.level[v]
        for n in adj[0][v]:
            self.level[n] = max(self.level[n], l)
        for n in adj[1][v]:
            self.level[n] = max(self.level[n], l)   

    def forward_dijkstra(self, v, stopping_distance):
        hop_limit = 5
        shortcut_count = 0
        shortcuts = set()
        shortcut_group = set()
        processed = set()
        dist = {}
        
        for p in self.adj[1][v]:
            if self.contracted[p]: continue
            h = []
            heapq.heappush(h, (0,p,0))
            dist[p] = 0
            while(len(h)):
                d, u, hops = heapq.heappop(h)
                
                if (d > stopping_distance):
                    break
                if u in processed or u == v or self.contracted[u] or hops == hop_limit: 
                    continue
                for idx, w in enumerate(adj[0][u]):
                    if w == v or self.contracted[w]:
                        continue
                    c = cost[0][u][idx]
                    if dist.get(w) == None:
                        dist[w] = self.INFINITY
                    if dist[w] > dist[u] + c:
                        dist[w] = dist[u] + c
                        heapq.heappush(h, (dist[w], w, hops+1))
                processed.add(v)
            
            for s in self.adj[0][v]:
                if self.contracted[s]: continue
                p_cost = self.INFINITY
                s_cost = self.INFINITY
                for idx, y in enumerate(self.adj[0][v]):
                    if y == s:
                        s_cost = min(s_cost, self.cost[0][v][idx])
                for idx, y in enumerate(self.adj[1][v]):
                    if y == p:
                        p_cost = min(p_cost, self.cost[1][v][idx])
                if dist.get(s) == None:
                        dist[s] = self.INFINITY
                short_cut_cost = p_cost + s_cost
                if short_cut_cost < dist[s]:
                    shortcuts.add((p,s,short_cut_cost))
                    shortcut_group.add(p)
                    shortcut_group.add(s)
                    shortcut_count += 1

            processed.clear()
            dist.clear()

        
        shortcut_cover = len(shortcut_group)
        
        return shortcut_count, shortcut_cover, shortcuts             
    
    def witness_search(self, v):
        shortcut_count, shortcut_cover, shortcuts = self.forward_dijkstra(v, self.stopping_distances[v])
         
        contracted_neighbors = set()
        for n in self.adj[0][v]:
            if self.contracted[n]:
                contracted_neighbors.add(n)
        for n in self.adj[1][v]:
            if self.contracted[n]:
                contracted_neighbors.add(n)
        cneighbors = len(contracted_neighbors)

        level = self.level[v]

        importance = (shortcut_count - len(self.adj[0][v]) - len(self.adj[1][v])) + cneighbors + shortcut_cover + level
        
        return importance, shortcuts

    def mark_visited(self, x):
        if not self.visited[x]:
            self.visited[x] = True
            self.visited.append(x)

    def add_arc(self, u, v, c):
        def update(adj, cost, u, v, c):
            for i in range(len(adj[u])):
                if adj[u][i] == v:
                    cost[u][i] = min(cost[u][i], c)
                    return
            adj[u].append(v)
            cost[u].append(c)

        update(self.adj[0], self.cost[0], u, v, c)
        update(self.adj[1], self.cost[1], v, u, c)

    # See description of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.workset:
            self.bidistance[0][v] = self.bidistance[1][v] = self.INFINITY
            self.visited[0][v] = self.visited[1][v] = False
        self.workset.clear()

    # See description of this method in the starter for friend_suggestion
    def visit(self, q, side, v, dist):
        # Implement this method yourself
        if self.bidistance[side][v] > dist:
            self.bidistance[side][v] = dist
            heapq.heappush(q[side], (dist, v))
        return

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        if s == t: return 0
        self.clear()
        q = [[], []]
        estimate = self.INFINITY
        self.visit(q, 0, s, 0)
        self.visit(q, 1, t, 0)
        self.workset.add(s)
        self.workset.add(t)
        d1 = 0 
        #print(self.rank)
        #print(self.adj[0], self.cost[0])
        # Bidirectional Dijkstra
        while(len(q[0]) or len(q[1])):
            for i in range(2):
                if(not len(q[i])):
                    continue

                d1, v = heapq.heappop(q[i])
                
                if d1 <= estimate and not self.visited[i][v]:
                    for idx, n in enumerate(self.adj[i][v]):
                        if self.rank[n] > self.rank[v]:
                            dist = self.cost[i][v][idx] + self.bidistance[i][v]
                            self.visit(q, i, n, dist)
                            self.workset.add(n) 
                    self.visited[i][v] = True

                if self.visited[(i+1)%2][v] and estimate > self.bidistance[i][v] + self.bidistance[(i+1)%2][v]:
                        estimate = self.bidistance[i][v] + self.bidistance[(i+1)%2][v]
        #print(self.rank)
        #print(self.bidistance[0], self.bidistance[1])        
        return -1 if estimate == self.INFINITY else estimate


INF = 10 ** 9


# Returns the adjacency matrix of a graph on the given vertices with edges equal to the distances between
# those nodes in the initial road network
def make_graph(ch, vertices):
    n = next(vertices)
    vertices = list(vertices)
    assert n == len(vertices)
    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            l = ch.query(vertices[i]-1, vertices[j]-1)
            graph[i][j] = l if l != -1 else INF
    return graph


# Returns the length of the shortest circular path visiting all the nodes at least once
def optimal_path(graph):
    #print(graph)
    n = len(graph)
    dp = {}

    #set initial state
    for i in range(1,n):
        subset_bit_mask = 1 << i
        dp[(i, subset_bit_mask)] = graph[0][i]
    

    for subset_size in range(2,n):
        for subset in itertools.combinations(range(1,n), subset_size):

            #set bits
            subset_bit_mask = 0
            for num in subset:
                subset_bit_mask |= 1 << num
            
            
            for num in subset:
                prev_bit_mask = subset_bit_mask & ~(1 << num)
            
                dists = []
                for j in subset:
                    if j == num: continue
                    a = dp[(j, prev_bit_mask)]
                    b = graph[j][num]
                    if a == INF or b == INF:
                        dists.append(INF)
                    else:    
                        dists.append(a+b)
                    dp[(num, subset_bit_mask)] = min(dists)
    
    dists = [] 
    prev_bit_mask = (2**n - 1) - 1
    for j in range(1,n):
        a = dp[(j, prev_bit_mask)]
        b = graph[j][0]
        if a == INF or b == INF:
            dists.append(INF)
        else:    
            dists.append(a+b)
        result = min(dists)

    return -1 if result == INF else result


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

    ch = DistPreprocessLarge(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for i in range(t):
        print(optimal_path(make_graph(ch, readl())))
