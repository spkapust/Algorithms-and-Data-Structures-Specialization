#Uses python3

import sys
import math

def negative_cycle(adj, cost):
    discovered = [False] * len(adj)
    for v in range(len(discovered)):
        if discovered[v] == False:
            discovered[v] = True
        else:
            continue
            
        #Bellman-Ford
        dist = [math.inf] * len(adj)
        dist[v] = 0

        for i in range(len(adj)):
            relaxed = False

            for j in range(len(adj)):
                for k in range(len(adj[j])):
                    u = j
                    n = adj[j][k]
                    c = cost[j][k]

                    #relax
                    discovered[n] = True
                    if dist[n] > dist[u] + c:
                        dist[n] = dist[u] + c
                        relaxed = True
            
            if relaxed == False:
                break
            elif i == len(adj) - 1:
                return 1

    return 0


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
    print(negative_cycle(adj, cost))
