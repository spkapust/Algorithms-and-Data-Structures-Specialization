#Uses python3

import sys


def bipartite(adj):
    label = [None] * len(adj)
    current_layer = []
    next_layer = []

    for v in range(len(adj)):
        if label[v] == None:
            label[v] = True
            current_layer.append(v)
            while(len(current_layer)):
                v = current_layer.pop()
                for n in adj[v]:
                    if label[n] == None:
                        next_layer.append(n)
                        label[n] = not label[v]
                    elif label[n] == label[v]:
                        return 0
                if(not len(current_layer)):
                    current_layer, next_layer = next_layer, current_layer
    #print(label)
    return 1

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
    print(bipartite(adj))
