# python3

import sys

# Vertex of a splay tree
class Vertex:
  def __init__(self, char, size, left, right, parent):
    (self.char, self.size, self.left, self.right, self.parent) = (char, size, left, right, parent)

#Splay tree implementation 
def get_size(v):
    if v == None: 
        return 0
    return v.size

def update(v):
  if v == None:
    return
  v.size = get_size(v.left) + get_size(v.right) + 1
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v


def find(root, index): 
    if root == None: return None
    v = root
    while True:
        if v == None: 
            return None
        else: 
            ls = get_size(v.left)
        if ls == index:
            return splay(v)
        elif index > ls:
            index -= (ls + 1)
            v = v.right
        else: 
            v = v.left

def split(root, index):  
    if root == None: 
        return (root, None)
    v = root
    root = find(root,index)
    if root == None:
        return (v, None)
    right = root
    left = right.left
    right.left = None
    if left != None: 
        left.parent = None
    update(left)
    update(right)
    return (left, right)
 
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

class Rope:
    
    def __init__(self, s):
        global root
        self.s = s
        for idx, char in enumerate(self.s):
            v = Vertex(char, idx+1, root, None, None)
            if root != None:
                root.parent = v
            root = v

    #Naive Code (still passes grader)   
    def naive_result(self):
        return self.s
    
    def naive_process(self, i, j, k):
        j = j + 1
        beginning = self.s[0:i]
        cut = self.s[i:j]
        end = self.s[j: len(self.s)]
        remaining = beginning + end
        if k == 0:
            self.s = cut + remaining
        else:
            beginning = remaining[0:k]
            end = remaining[k:len(remaining)]
            self.s = beginning + cut + end

    def result(self):
        global root
        #iterative in order traversal
        current = root
        stack = []
        #traversal = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.char, end='')
                #traversal.append(current.char)
                current = current.right
            else:
                print('')
                break
        #print(traversal)
        return #''.join(traversal)

    def process(self, i, j, k):
        global root
        left, middle = split(root, i)
        cut, right = split(middle, j-i+1)
        reassemble = merge(left, right)
        left, right = split(reassemble, k)
        root = merge(merge(left,cut), right)
        return
                
global root 
root = None
rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
#print(rope.result())
rope.result()

