#python3
import itertools
from sys import stdin 

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))


def printEquisatisfiableSatFormula(n,m,A,b):
  clauses = []

  # c=[]
  # for i in range(m):
  #   c.append(i+1)
  # clauses.append(c)

  guaranteed_unsatisfiable=False
  for i, inequality in enumerate(A):
    variables = []
    coefs = []
    for j, coef in enumerate(inequality):
      if coef != 0:
        variables.append(j+1)
        coefs.append(coef)
    
    if len(coefs) == 0 and b[i] < 0:
      guaranteed_unsatisfiable = True
      print(2, 1)
      print(1, 0)
      print(-1, 0)
      break

    for combination in itertools.product(range(2), repeat=len(coefs)):
      
      if sum(x*y for x,y in zip(coefs, combination)) > b[i]:
        clause = []
        for idx, c in enumerate(combination):
          if c == 0:
            clause.append(variables[idx])
          else:
            clause.append(-variables[idx])
        clauses.append(clause)
        #print('combo', list(zip(coefs, combination)))

  if not guaranteed_unsatisfiable:
    if len(clauses) == 0:
      print(1,1)
      print(1, 0)
    else:
      print(len(clauses), m)
      for clause in clauses:
        print(' '.join(map(str, clause)), end = ' ')
        print(0)
    

printEquisatisfiableSatFormula(n,m,A,b)
