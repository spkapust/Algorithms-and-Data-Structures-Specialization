#Uses python3

import sys

def explore(adj, visited, recursion_visited, v):
    visited[v] = True
    recursion_visited[v] = True
    for n in adj[v]:
        if recursion_visited[n]:
            return False
        elif not explore(adj, visited, recursion_visited, n):
            return False
    recursion_visited[v] = False
    return True

def acyclic(adj):
    visited = [False] * len(adj)
    recursion_visited = [False] * len(adj)
    for v in range(len(adj)):
        if not visited[v]:
            if not explore(adj, visited, recursion_visited, v):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
