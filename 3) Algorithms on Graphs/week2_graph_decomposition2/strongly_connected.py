#Uses python3

import sys

sys.setrecursionlimit(200000)

def reverse_edges(adj):
    rev = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for e in adj[i]:
            rev[e].append(i)
    return rev

def dfs(adj, visited, processed, pv, v, clock):
    stack = []
    stack.append(v)
    while(len(stack)):
        v = stack[-1]
        #print(list(map(lambda x: x+1, stack)))
        if (not visited[v]) and (not processed[v]):
            for n in adj[v]:
                if not visited[n]:
                    stack.append(n)
            visited[v] = True
        elif visited[v] and (not processed[v]):
            stack.pop()
            #postvisit
            pv[v] = clock
            clock += 1
            processed[v] = True
        elif visited[v] and processed[v]:
            stack.pop()
    return clock
    
def toposort(adj):
    clock = 0
    visited = [False] * len(adj)
    processed = [False] * len(adj)
    pv = [0] * len(adj)

    for v in range(len(adj)):
        if not visited[v]:
           clock = dfs(adj, visited, processed, pv, v, clock)
    
    order = list(reversed(sorted(range(len(pv)), key=lambda k: pv[k])))
    return order

def iter_explore(adj, visited, v):
    stack = []
    stack.append(v)
    while(len(stack)):
        v = stack[-1]
        if not visited[v]:
            for n in adj[v]:
                if not visited[n]:
                    stack.append(n)
            visited[v] = True
        elif visited[v]:
            stack.pop()
    return 


def number_of_strongly_connected_components(adj):
    rev = reverse_edges(adj)
    order = toposort(rev)
    visited = [False] * len(adj)
    scc = 0
    #print(order)
    for v in order:
        if not visited[v]:
            iter_explore(adj, visited, v)
            scc += 1
    return scc

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
