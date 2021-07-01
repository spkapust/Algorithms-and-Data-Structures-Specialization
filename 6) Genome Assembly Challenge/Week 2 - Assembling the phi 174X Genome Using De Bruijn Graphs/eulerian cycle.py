#python3
import sys

input = sys.stdin.readline()
nodes, edges = list(map(int, input.split()))

adj = [[] for _ in range(nodes)]
in_degree = [0 for _ in range(nodes)]
out_degree = [0 for _ in range(nodes)]

for _ in range(edges):
    input = sys.stdin.readline()
    a, b = list(map(int, input.split()))
    a,b = a-1, b-1
    adj[a].append(b)
    out_degree[a] += 1
    in_degree[b] += 1

imbalanced = False
for n in range(nodes):
    if in_degree[n] != out_degree[n]:
        imbalanced = True
        print(0)
        break

if not imbalanced:
    edge_count = dict()
  
    for i in range(len(adj)):
        edge_count[i] = len(adj[i])
  
    curr_path = []
    circuit = []
    curr_path.append(0)
  
    while len(curr_path):
        curr_v = curr_path[-1]
        if edge_count[curr_v]:
            next_v = adj[curr_v][-1]
            curr_path.append(next_v)
  
            edge_count[curr_v] -= 1
            adj[curr_v].pop()
        else:
            circuit.append(curr_v)
            curr_path.pop()
  
    # we've got the circuit, now print it in reverse
    print(1)
    for i in reversed(circuit[1:]):
        print(i + 1, end = " ")
        