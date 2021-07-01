# python3

# Arguments:
#   * `n` - the number of vertices.
#   * `edges` - list of edges, each edge is a tuple (u, v), 1 <= u, v <= n.
#   * `colors` - list consisting of `n` characters, each belonging to the set {'R', 'G', 'B'}.
# Return value: 
#   * If there exists a proper recoloring, return value is a list containing new colors, similar to the `colors` argument.
#   * Otherwise, return value is None.

def assign_new_colors(n, edges, colors):
    clauses = generate_2sat_clauses(colors, edges)
    if clauses == None: return None
    result = efficient_2sat(n*3, clauses)
    if result == None: return None
    new_colors = []
    for i in range(0, n*3, 3):
        if not result[i]:
            new_colors.append("R")
        elif not result[i+1]:
            new_colors.append("G")
        else: #result[i+1]
            new_colors.append("B")
    
    return new_colors
    

def generate_2sat_clauses(colors, edges):
    clauses = []
    for idx, c in enumerate(colors):
        v = idx+1
        r = v*3-2
        g = r + 1
        b = g + 1
        if c == "R":
            clauses.append([-r, -r])
            clauses.append([g, b])
            clauses.append([-g, -b])
        elif c == "G":
            clauses.append([-g, -g])
            clauses.append([r, b])
            clauses.append([-r, -b])
            pass
        else: #c == "B"
            clauses.append([-b, -b])
            clauses.append([r, g])
            clauses.append([-r, -g])

    for a,b in edges:
        if a == b:
            return None
        ar = a*3-2
        ag = ar + 1
        ab = ag + 1
        br = b*3-2
        bg = br + 1
        bb = bg + 1
        clauses.append([-ar, -br])
        clauses.append([-ag, -bg])
        clauses.append([-ab, -bb])
    
    return clauses  

def c_to_adj(v,n):
    if v < 0:
        return -v-1
    else:
        return v-1+n

def efficient_2sat(n, clauses):
      
    #build graph                                 
    num_nodes = 2*n
    adj = [[] for _ in range(num_nodes)]
    
    for clause in clauses:
        a,b = clause
        adj[c_to_adj(-a,n)].append(c_to_adj(b,n))
        if a!=b:
            adj[c_to_adj(-b,n)].append(c_to_adj(a,n))
    #print(adj)

    result = [False] * n
    assigned = [False] * n
    
    #Iterative Tarjan's
    v_id = 1
    scc_count = 1
    ids =  [0] * num_nodes
    lows = [0] * num_nodes
    sccs = [0] * num_nodes
    
    processed = [False] * num_nodes
    on_tarjan_stack = [False] * num_nodes
    tarjan_stack = []
    dfs_stack = []

    for v in range(num_nodes):
        if not processed[v]:
            dfs_stack.append(v)
            
            while(len(dfs_stack)):
                at = dfs_stack[-1]
                
                if processed[at]: 
                    dfs_stack.pop()
                    continue
                
                if ids[at] == 0:
                    tarjan_stack.append(at)
                    on_tarjan_stack[at] = True
                    ids[at] = v_id
                    lows[at] = v_id
                    v_id += 1
                    recurse = False
                    for to in adj[at]:
                        if ids[to] == 0:
                            dfs_stack.append(to)
                            recurse=True
                    if recurse:
                        continue
                
                for to in adj[at]:
                   if on_tarjan_stack[to]:
                       lows[at] = min(lows[at], lows[to])
                        

                if ids[at] == lows[at]:
                    assigned_scc = False
                    for t in reversed(tarjan_stack):
                        if (t < n and assigned[t]) or (t>=n and assigned[t-n]):
                                assigned_scc = True
                                break
                        if t == at:
                            break
                    
                    while(len(tarjan_stack)):
                        t = tarjan_stack.pop()
                        on_tarjan_stack[t]=False
                        lows[t] = ids[at]
                        sccs[t] = scc_count
                        if t < n:
                            assigned[t] = True
                            result[t] = not assigned_scc
                        else:
                            assigned[t-n] = True
                            result[t-n] = assigned_scc
                        if t == at: 
                            break

                    scc_count += 1
                
                
                processed[at] = True
                dfs_stack.pop()
                
    for i in range(n):
        if sccs[i] == sccs[i+n]:
            return None

    return result

    
def main():
    n, m = map(int, input().split())
    colors = input()
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    new_colors = assign_new_colors(n, edges, colors)
    if new_colors is None:
        print("Impossible")
    else:
        print(''.join(new_colors))

main()
