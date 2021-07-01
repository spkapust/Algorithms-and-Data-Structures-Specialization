# python3
from sys import stdin
import math

def augment_table(n, A, b, c):
  #add slack variables
  for i in range(n):
    for j in range(n):
      if j == i:
        A[i].append(1)
      else:
        A[i].append(0)
    #add z
    A[i].append(0)
  
  #print('added slack')
  #print(A)
  
  #add last row
  A.append(c)
  for i, _ in enumerate(A[n]):
    A[n][i] = -1*A[n][i]
  
  #print('added c')
  #print(A)
  for i in range(n):
    A[n].append(0)
  A[n].append(1)

  b.append(0)

def negative_element_exists(n,A):
  for e in A[n]:
    if e < 0:
      return True
  return False

def get_pivot_element(n,A,b):
  minimum = min(A[n])
  potential_columns = []
  for idx, value in enumerate(A[n]):
    if value == minimum:
      potential_columns.append(idx)
  
  #smallest non-negative
  snn = math.inf
  for c in potential_columns:
    for r in range(n):
      if A[r][c] == 0: continue
      #print(r,c)
      result = b[r] / A[r][c]
      if result < snn and result >= 0:
        snn = result
        pivot_row = r
        pivot_column = c
  return (pivot_row, pivot_column)

def reduce(n,A,b,r,c):
  #Divide out so pivot element is equal to 1
  value = A[r][c]
  A[r] = [x / value for x in A[r]]
  b[r] = b[r] / value

  #Adjust values in all other rows
  for idx, row in enumerate(A):
      if idx == r:
          continue
      multiplier = row[c]
      for i in range(len(row)):
          #print(row, len(row))
          #print(r,i)
          row[i] -= multiplier * A[r][i]
      b[idx] -= multiplier * b[r]

def is_basic_column(A, c):
  encountered_one = False
  for r in range(len(A)):
    if A[r][c] == 0:
      continue
    elif A[r][c] == 1:
      if encountered_one == False: 
        encountered_one = True
        row = r
      else:
        return (False, 0)
    else:
      return (False,0)
  return (True, row)



def allocate_ads(n, m, A, b, c):
  
  augment_table(n,A, b, c.copy())
  
  while(negative_element_exists(n,A)):
    r, c = get_pivot_element(n,A,b)
    reduce(n,A,b,r,c)
    
  
  result = []
  for i in range(m):
    status, row = is_basic_column(A,i)
    if status:
      result.append(b[row])
    else:
      result.append(0)
  
  return [0, result]

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = allocate_ads(n, m, A, b, c)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")
    
