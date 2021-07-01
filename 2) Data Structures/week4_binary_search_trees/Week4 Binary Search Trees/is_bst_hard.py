#!/usr/bin/python3

import sys, threading
import math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size, had to increase this from 2**25 for it to pass the grader

def inOrderRec(tree, index, min_key, max_key):
  if not (min_key <= tree[index][0] < max_key): return False

  hasLeft = True if tree[index][1] != -1 else False
  hasRight = True if tree[index][2] != -1 else False
  
  l = True if not hasLeft else inOrderRec(tree, tree[index][1], min_key, tree[index][0])
  if not l: return False
  
  r = True if not hasRight else inOrderRec(tree, tree[index][2], tree[index][0], max_key)
  if not r: return False
  
  return True

def IsBinarySearchTree(tree):
  if not tree: return True
  return inOrderRec(tree, 0, -math.inf, math.inf)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
