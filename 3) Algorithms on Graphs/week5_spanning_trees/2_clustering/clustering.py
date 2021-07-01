#Uses python3
import sys
import math


class DisjSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
  
  
    # Finds set of given item x
    def find(self, x):
          
        # Finds the representative of the set
        # that x is an element of
        if (self.parent[x] != x):
              
            # if x is not the parent of itself
            # Then x is not the representative of
            # its set,
            self.parent[x] = self.find(self.parent[x])
              
            # so we recursively call Find on its parent
            # and move i's node directly under the
            # representative of this set
  
        return self.parent[x]
  
  
    # Do union of two sets represented
    # by x and y.
    def Union(self, x, y):
          
        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)
  
        # If they are already in same set
        if xset == yset:
            return
  
        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
  
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
  
        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1]-p1[1])**2)

def clustering(x, y, k):
    ds = DisjSet(len(x))
    sets = len(x)
    edges = []
    for i in range(len(x)):
        for j in range(i, len(x)):
            p1 = (x[i],y[i])
            p2 = (x[j],y[j])
            edges.append((dist(p1,p2),(i,j)))
    edges.sort()
    for e in edges:
        i = e[1][0]
        j = e[1][1]
        if ds.find(i) != ds.find(j):
            if sets == k:
                return e[0]
            ds.Union(i,j)
            sets-=1

    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
