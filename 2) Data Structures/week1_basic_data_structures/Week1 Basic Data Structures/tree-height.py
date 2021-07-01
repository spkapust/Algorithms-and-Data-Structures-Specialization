# python3
from collections import deque
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self):
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
    
    def get_children(self):
        return self.children
    
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
    
    def get_num_children(self):
        return len(self.children)


class Tree:
    def __init__(self):
        #Take inputs
        self.n = int(sys.stdin.readline())
        children = list(map(int, sys.stdin.readline().split()))

        #Build tree
        self.nodes = [Node() for i in range(self.n)]
        for child_index, parent_index in enumerate(children):
            self.nodes[child_index].set_data(parent_index)
            if parent_index == -1:
                self.root = self.nodes[child_index]
            else:
                self.nodes[parent_index].add_child(self.nodes[child_index])
        

    def compute_height(self):
        if len(self.nodes) == 0: return 0
        else:
            q = deque()
            q.append(self.root)
         
            while len(q) > 0:
                last = q.popleft()
                for c in last.get_children():
                    q.append(c)

            height = 1
            while last != self.root:
                height += 1
                parent = last.get_data()
                last = self.nodes[parent]

        return height

def main():
  tree = Tree()
  print(tree.compute_height())

threading.Thread(target=main).start()
