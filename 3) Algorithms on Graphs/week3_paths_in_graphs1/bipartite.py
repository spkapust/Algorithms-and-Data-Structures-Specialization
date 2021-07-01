#Uses python3

import sys
import queue

def bipartite(adj):
    label = [None] * len(adj)
    q = queue.Queue()

    for v in range(len(adj)):
        if label[v] == None:
            label[v] = True
            q.put(v)
            while(not q.empty()):
                v = q.get()
                for n in adj[v]:
                    if label[n] == None:
                        q.put(n)
                        label[n] = not label[v]
                    elif label[n] == label[v]:
                        return 0
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
