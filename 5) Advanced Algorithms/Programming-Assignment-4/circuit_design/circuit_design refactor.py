# python3
n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]

# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
def isSatisfiable():
    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

def c_to_adj(v,n):
    if v < 0:
        return -v-1
    else:
        return v-1+n



def efficient_is_satisfiable():
      
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

    
result = efficient_is_satisfiable()
if result is None:
    print("UNSATISFIABLE")
else:
    print("SATISFIABLE")
    print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))
