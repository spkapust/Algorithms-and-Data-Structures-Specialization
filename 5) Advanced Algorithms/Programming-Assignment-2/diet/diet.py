# python3
from sys import stdin
import itertools
import math

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column] or a[pivot_element.row][pivot_element.column] == 0:
        pivot_element.column += 1
        if pivot_element.column == len(used_columns):
          return pivot_element
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column

def ProcessPivotElement(a, b, pivot_element):

    #Divide out so pivot element is equal to 1
    value = a[pivot_element.row][pivot_element.column]
    a[pivot_element.row] = [x / value for x in a[pivot_element.row]]
    b[pivot_element.row] = b[pivot_element.row] / value

    #Adjust values in all other rows
    for idx, row in enumerate(a):
        if idx == pivot_element.row:
            continue
        multiplier = row[pivot_element.column]
        for i in range(pivot_element.column, len(row)):
            row[i] -= multiplier * a[pivot_element.row][i]
        b[idx] -= multiplier * b[pivot_element.row]

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for _ in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        if pivot_element.column == size:
            if b[pivot_element.row] == 0:
              return 0
            else:
              return -1
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b

def dot(v1, v2):
  return sum(x*y for x, y in zip(v1, v2))

def solve_diet_problem(n, m, A, b, c):
  epsilon = 10**-3
  
  for idx in range(m):
    b.append(0)
    inequality = [0] * m
    inequality[idx] = -1
    A.append(inequality)
  A.append([1] * m)
  b.append(10**9)
  
  anst = -1
  best = -math.inf
  bests = [0] * m 
  for comb in itertools.combinations(range(n+m+1), m):
    ea = []
    eb = []
    for i in comb:
      ea.append(A[i].copy())
      eb.append(b[i])
    eq = Equation(ea, eb)
    
    s = SolveEquation(eq)
    if s == -1 or s == 0:
      continue
    
    if dot(s,c) > best:
      satisfies = True
      for i, val in enumerate(b):
        if dot(s,A[i]) - epsilon > val:
          satisfies = False
          break
      if satisfies:
        best = dot(s,c)
        bests = s
        if n+m in comb:
          anst = 1
        else:
          anst = 0

  return [anst, bests]

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, b, c)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")
    
