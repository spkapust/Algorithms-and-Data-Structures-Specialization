#python3

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]


def belongs_to_path(n, clauses):
    for v in range(1, n+1):
        c = []
        for p in (range(1,n+1)):
            c.append(v*n-n+p)
        clauses.append(c)

def appears_once_in_path(n, clauses):
    for v in range(1,n+1):
        for p1 in range(1,n+1):
            a = v*n-n+p1
            for p2 in range(p1+1, n+1):
                b = v*n-n+p2
                clauses.append([-a,-b])

def each_position_occupied(n, clauses):
    for p in range(1, n+1):
        c = []
        for v in range(1, n+1):
            c.append(v*n-n+p)
        clauses.append(c)

def do_not_occupy_same(n, clauses):
    for p in range(1, n+1):
        for v1 in range(1, n+1):
            v1p = v1*n-n+p
            for v2 in range(v1+1, n+1):
                v2p = v2*n-n+p
                clauses.append([-v1p, -v2p])

def not_next_to(n, edges, clauses):
    adjacency_table = {}
    for e in edges:
        adjacency_table[(e[0],e[1])] = True
        adjacency_table[(e[1],e[0])] = True
    for v1 in range(1,n+1):
        for v2 in range(1,n+1):
            if v2 == v1: 
                continue
            if adjacency_table.get((v1,v2)) != True:
                for p in range(1,n):
                    a = v1*n-n+p
                    b = v2*n-n+p+1
                    clauses.append([-a,-b])


def printEquisatisfiableSatFormula(n,m,edges):


    clauses = []
    belongs_to_path(n, clauses)
    #print('belongs to path')
    #print(clauses)
    appears_once_in_path(n, clauses)
    #print('appears once')
    #print(clauses)
    each_position_occupied(n, clauses)
    #print('each occupied')
    #print(clauses)
    do_not_occupy_same(n, clauses)
    #print('do not occupy same')
    #print(clauses)
    not_next_to(n,edges,clauses)

    print(len(clauses), n*n)
    for c in clauses:
        print(' '.join(map(str, c)), end = ' ')
        print(0)
    
    



printEquisatisfiableSatFormula(n,m, edges)
