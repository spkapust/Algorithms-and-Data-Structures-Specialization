#Uses python3

import sys
import queue
import math


def shortest_paths(adj, cost, s, distance, reachable, shortest):
    
    #BFS to find reachable from s
    reachable[s] = 1
    current_layer = []
    next_layer = []
    current_layer.append(s)
    while(len(current_layer)):
        v = current_layer.pop()
        for n in adj[v]:
            if reachable[n] == 0:
                next_layer.append(n)
                reachable[n] = 1
        if(not len(current_layer)):
            current_layer, next_layer = next_layer, current_layer


    #Bellman-Ford
    distance[s] = 0
    a = set()
    for i in range(len(adj)):
        relaxed = False

        for j in range(len(adj)):
            for k in range(len(adj[j])):
                u = j
                n = adj[j][k]
                c = cost[j][k]

                #relax
                if reachable[n] == 1 and distance[n] > distance[u] + c:
                    distance[n] = distance[u] + c
                    relaxed = True
                    if i == len(adj) - 1:
                        a.add(n)

        if relaxed == False:
            break
        
    #BFS reachable from A
    for u in a:
        if shortest[u] == 0:
            continue
        
        shortest[u] = 0
        current_layer.append(u)
        while(len(current_layer)):
            v = current_layer.pop()
            for n in adj[v]:
                if shortest[n] == 1:
                    next_layer.append(n)
                    shortest[n] = 0
            if(not len(current_layer)):
                current_layer, next_layer = next_layer, current_layer

    return


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

