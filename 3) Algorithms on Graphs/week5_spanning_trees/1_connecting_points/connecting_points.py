#Uses python3
import sys
import math
import heapq

def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1]-p1[1])**2)


def minimum_distance(x, y):
    visited = [False] * len(x)

    pq = [(0,0)]
    distance = 0
    num_visited = 0 
    while(len(pq)):
       v = heapq.heappop(pq)
       i = v[1]
       if visited[i] == True:
           continue
       visited[i] = True

       distance += v[0]
       num_visited += 1
       if num_visited == len(x):
           break
       
       p1 = (x[i], y[i])
       for i in range(len(x)):
           if visited[i] == False:
            p2 = (x[i],y[i])
            heapq.heappush(pq, (dist(p1, p2), i)) 
            #print(pq)   
   
    return distance


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
