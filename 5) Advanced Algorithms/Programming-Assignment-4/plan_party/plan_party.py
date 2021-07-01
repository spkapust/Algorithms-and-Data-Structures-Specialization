#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent, memo):
    #print(vertex, parent)
    if memo[vertex] != -1:
        return memo[vertex]
    if len(tree[vertex].children) == 1 and tree[vertex].children[0] == parent:
        return tree[vertex].weight
    else:
        m1 = tree[vertex].weight
        for child in tree[vertex].children:
            if child != parent:
                for grandchild in tree[child].children:
                    if grandchild != vertex:
                        m1 += dfs(tree, grandchild, child, memo)
        m0 = 0
        for child in tree[vertex].children:
            if child != parent:
               m0 += dfs(tree, child, vertex, memo)
        memo[vertex] = max(m0,m1)
        return memo[vertex]
            

    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    memo = [-1] * size
    return dfs(tree, 0, -1, memo)
    


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
