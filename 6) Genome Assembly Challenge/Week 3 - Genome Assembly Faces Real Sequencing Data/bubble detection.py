# python3

import sys
import itertools

k, t, *reads = sys.stdin.read().split()
k, t = int(k), int(t)
read_length = len(reads[0])

#Build Graph
db_graph = {}
for read in reads:
    for i in range(read_length-k+1):
        kmer = read[i:i+k]
        from_ = kmer[:-1]
        to = kmer[1:]
        if from_ != to:
            db_graph.setdefault(from_, [set(), 0])
            db_graph.setdefault(to, [set(), 0]) 
            if to not in db_graph[from_][0]:
                db_graph[from_][0].add(to)
                db_graph[to][1] += 1

def dfs(path, start, current, depth):
    outgoing_set, num_incoming = db_graph[current]
    if num_incoming > 1:
        paths.setdefault((start, current), list())
        paths[(start,current)].append(path[:])

    if depth == t:
        return

    for next_ in outgoing_set:
        if next_ not in path:
            path.append(next_)
            dfs(path, start, next_, depth + 1)
            path.remove(next_)

paths = {}
for key, value in db_graph.items():
    outgoing_set, incoming = value
    if len(outgoing_set) > 1:
        dfs([key], key, key, 0)

bubbles = 0
for _, candidates_list in paths.items():
    for pair in itertools.combinations(candidates_list, r=2):
            if len(set(pair[0]) & set(pair[1])) == 2:
                bubbles += 1

print(bubbles)

