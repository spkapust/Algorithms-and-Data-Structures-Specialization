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

def efficient_is_satisfiable():
    result = [False] * n
    assigned = [False] * n
    #build graph                                      -vn          -v1      v1  v2          vn
    #edge graph mapping looks like this------------>   0  1 .....  n-1   n  n+1 n+2 .......n+n
    #notice adj[n] is unoccupied because that would correspond to a variable being 0. Hence, always add 1 to num_nodes
    num_nodes = 2*n
    adj = [[] for _ in range(num_nodes+1)]
    for clause in clauses:
        a,b = clause
        adj[n-a].append(n+b)
        if a!=b:
            adj[n-b].append(n+a)
    #print(adj)
    
    #Iterative Tarjan's
    unvisited = -1
    id = 0
    scc = 0
    ids = [unvisited] * (num_nodes+1)
    lows = [0] * (num_nodes+1)
    sccs = [0] * (num_nodes+1)
    #ids[n] = None
    #lows[n] = None
    #sccs[n] = None
    #scanned = [False] *(num_nodes+1)
    processed = [False] *(num_nodes+1)
    on_tarjan_stack = [False] * (num_nodes+1)
    tarjan_stack = []
    iter_stack = []


    for v in range(num_nodes+1):
        if ids[v] == unvisited and v != n:
            iter_stack.append(v)
            
            while(len(iter_stack)):
                at = iter_stack[-1]
                
                if processed[at]: 
                    iter_stack.pop()
                    continue
                
                if ids[at] == unvisited:
                    tarjan_stack.append(at)
                    on_tarjan_stack[at] = True
                    ids[at] = id
                    lows[at] = id
                    id+=1
                    going_deeper = False
                    for to in adj[at]:
                        if ids[to] == unvisited:
                            iter_stack.append(to)
                            going_deeper=True
            
                    if going_deeper:
                        continue
                
                for to in adj[at]:
                   if on_tarjan_stack[to]:
                       lows[at] = min(lows[at], lows[to])
                        

                if ids[at] == lows[at]:
                    #print('new component at', at-n)
                    #print('tarjan', tarjan_stack)
                    assigned_component = False
                    i = -1
                    while(len(tarjan_stack)):
                        t = tarjan_stack[i]
                        if (t < n and assigned[n-t-1]) or (t > n and assigned[t-n-1]):
                                assigned_component = True
                                break
                        if t == at:
                            break
                        i -= 1
                    
                    while(len(tarjan_stack)):
                        t = tarjan_stack.pop()
                        on_tarjan_stack[t]=False
                        lows[t] = ids[at]
                        sccs[t] = scc
                        if t < n:
                            assigned[n-t-1] = True
                            result[n-t-1] = not assigned_component
                        else:
                            assigned[t-n-1] = True
                            result[t-n-1] = assigned_component
                        if t == at: 
                            break

                    scc += 1
                
                
                processed[at] = True
                iter_stack.pop()
                
    
    
    for i in range(1, n+1):
        if sccs[n+i] == sccs[n-i]:
            return None

    return result

    
result = efficient_is_satisfiable()
if result is None:
    print("UNSATISFIABLE")
else:
    print("SATISFIABLE")
    print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))
