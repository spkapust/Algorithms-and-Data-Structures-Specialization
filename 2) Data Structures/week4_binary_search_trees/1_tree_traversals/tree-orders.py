# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrderRecurse(self, result, index):
    if self.left[index] != -1: self.inOrderRecurse(result, self.left[index])
    result.append(self.key[index])
    if self.right[index] != -1: self.inOrderRecurse(result, self.right[index])

  def inOrder(self):
    self.result = []
    self.inOrderRecurse(self.result, 0)
    return self.result

  def preOrderRecurse(self, result, index):
    result.append(self.key[index])
    if self.left[index] != -1: self.preOrderRecurse(result, self.left[index])
    if self.right[index] != -1: self.preOrderRecurse(result, self.right[index])

  def preOrder(self):
    self.result = []
    self.preOrderRecurse(self.result, 0)        
    return self.result

  def postOrderRecurse(self, result, index):
    if self.left[index] != -1: self.postOrderRecurse(result, self.left[index])
    if self.right[index] != -1: self.postOrderRecurse(result, self.right[index])
    result.append(self.key[index])

  def postOrder(self):
    self.result = []
    self.postOrderRecurse(self.result, 0)         
    return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
