#Uses python3

import sys
import heapq
import math


def distance(adj, cost, s, t):
   #as an alternative to math.inf, 
   #find the maximum edge cost and multiply
   #by the number of vertexes-1 for the maximum potential cost
   
    dist = [math.inf] * len(adj)
    dist[s] = 0
    processed = [False] * len(adj)
    prev = [-1] * len(adj)

    #create min-heap
    h = []
    for i in range(len(dist)):
        heapq.heappush(h, (dist[i], i))
    
    while(len(h)):
        v = heapq.heappop(h)[1]
        
        if processed[v]: 
            continue

        if v == t:
            if dist[t] == math.inf:
                return -1
            else: 
                return dist[t] 

        for i in range(len(adj[v])):
            n = adj[v][i]
            c = cost[v][i]

            if dist[n] > dist[v] + c:
                dist[n] = dist[v] + c
                prev[n] = v
                heapq.heappush(h, (dist[n], n))
        
        processed[v] = True

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
