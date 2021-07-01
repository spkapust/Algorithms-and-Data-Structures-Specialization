#Uses python3
import sys
import math
import random

def minpoints(x,y,l,r):
    min_distance = math.inf
    if (r-l)<= 3:
        for i in range(l,r):
            for j in range(i+1,r):
                dsquared = (x[i][0]-x[j][0])**2 + (x[i][1]-x[j][1])**2
                min_distance = min(min_distance, dsquared)
        return min_distance
    
    half = l + ((r-l) // 2)
    minleft = minpoints(x,y,l,half)
    minright = minpoints(x,y,half,r)
    delta = min(minleft,minright)
    min_distance = delta
    if min_distance == 0: return 0

    median = (x[half][0] + x[half-1][0]) / 2

    strip = []
    for p in y:
        if (median - delta) < p[0] < (median + delta):
            strip.append(p)
        
    
    for i in range(len(strip)):
        compares = 0
        for j in range(i+1, len(strip)):
            if abs(strip[j][1]-strip[i][1]) >= min_distance: break
            dsquared = (strip[i][0]-strip[j][0])**2 + (strip[i][1]-strip[j][1])**2
            min_distance = min(min_distance, dsquared)
            compares +=1
            if compares == 4: break
    
    return min_distance
    

def minimum_distance(x, y):
    # sortedx = list(zip(x,y))
    # sortedx.sort()
    sortedx = []
    for i in range(len(x)):
        sortedx.append((x[i], y[i]))
    sortedy = sortedx.copy()
    sortedy.sort(key = lambda x: x[1])
    #print(sortedx)
    #print(sortedy)
    return math.sqrt(minpoints(sortedx, sortedy, 0, len(sortedx)))
    #return naive_min_distance(x,y)

def naive_min_distance(x,y):
    min_distance = math.inf
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            dsquared = (x[i]-x[j])**2 + (y[i]-y[j])**2
            min_distance = min(min_distance, dsquared)
    min_distance = math.sqrt(min_distance)
    return min_distance

if __name__ == '__main__':
    n = random.randint(0,1000)
    x = [random.randrange(-100,100) for i in range(n+1)]
    y = [random.randrange(-100,100) for i in range(n+1)]
    i=0
    sortedx = []
    for i in range(len(x)):
        sortedx.append((x[i], y[i]))
    sortedy = sortedx.copy()
    sortedy.sort(key = lambda x: x[1])
    while(i < 10000):
        a = naive_min_distance(x,y)
        b = minimum_distance(sortedx,sortedy)
        if a != b:
            points = []
            for i in range(len(x)):
                points.append((x[i], y[i]))
            print(points)
            print(a)
            print(b)
        i += 1
        break
    print("DONE")
  