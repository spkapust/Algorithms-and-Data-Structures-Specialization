# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

#Vertex 1 will be associated with 1,2,3 (1 different variable for each color)
#Vertex 2 will be associated with 4,5,6
#Vertex x will be associated with 3x-2, 3x-1, 3x
def printEquisatisfiableSatFormula(n, m, edges):
    
    #3 variables per vertex and 4 clauses per vertex + 3 clauses per edge
    clause_count = 4*n + 3*m
    var_count = n*3
    print(clause_count, var_count)

    #One color per vertex
    for i in range(1,n+1):
        c = 3*i
        b = c - 1
        a = b - 1
        print(a, b, c, 0)
        print(-a, -b, 0)
        print(-a, -c, 0)
        print(-b, -c, 0)
    
    #Connecting vertices must be different color
    #CNF of Nand(x,y) --> (-x | -y )
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        c1 = 3*v1
        b1 = c1 - 1
        a1 = b1 - 1
        c2 = 3*v2
        b2 = c2 - 1
        a2 = b2 - 1
        print(-a1, -a2, 0)
        print(-b1, -b2, 0)
        print(-c1, -c2, 0)

printEquisatisfiableSatFormula(n, m, edges)
