#Uses python3

import sys

def distance(adj, s, t):
    distance = [-1] * len(adj)
    distance[s] = 0
    current_layer = []
    next_layer = []
    
    current_layer.append(s)
    while(len(current_layer)):
        v = current_layer.pop()
        for n in adj[v]:
            if distance[n] == -1:
                next_layer.append(n)
                distance[n] = distance[v] + 1
        if(not len(current_layer)):
            current_layer, next_layer = next_layer, current_layer
            
    return distance[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
