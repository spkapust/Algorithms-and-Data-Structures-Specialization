#Uses python3

import sys

def infinite_sequence():
    c = 0
    while True:
        yield c
        c+=1

def dfs(adj, visited, pv, v):
    visited[v] = True
    for n in adj[v]:
        if not visited[n]:
            dfs(adj, visited, pv, n)
    
    #postvisit
    global clock
    pv[v] = clock
    clock += 1
    

def toposort(adj):
    global clock
    clock = 0
    visited = [False] * len(adj)
    pv = [0] * len(adj)

    for v in range(len(adj)):
        if not visited[v]:
            dfs(adj, visited, pv, v)
    #print(pv)
    order = list(reversed(sorted(range(len(pv)), key=lambda k: pv[k])))
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

