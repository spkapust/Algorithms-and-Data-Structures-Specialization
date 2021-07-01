#Uses python3
import sys
import math

def minimum_distance(x, y):
   
    length = len(x)
    min_distance = math.inf
   
    #Base Case#
    if length <= 3:
        for i in range(length - 1):
            for j in range(i+1, length):
                dsquared = (x[i][0]-x[j][0])**2 + (x[i][1]-x[j][1])**2
                min_distance = min(min_distance, dsquared)
        return min_distance
    

    #Split X and Y sorted sets at X's median#
    xmed = length // 2
    xl = x[:xmed]
    xr = x[xmed:]
    midx = x[xmed][0]

    # unsure how to properly decouple Ys
    # yl = []
    # yr = []
    # for p in y:
    #      if p[0] < midx:
    #          yl.append(p)
    #      else: yr.append(p)

    #Recursive Calls#
    minleft = minimum_distance(xl,y)
    minright = minimum_distance(xr,y)
    delta = min(minleft,minright)
    if delta == 0: return 0
    min_distance = delta


    #Create strip of all points within delta of median#
    strip = list()
    for p in y:
        if (midx - delta) < p[0] < (midx + delta):
            strip.append(p)
    
    #Compare all values in strip, only need to make 4 comparisons
    for i in range(len(strip)-1):
        for j in range(i+1, min(i+5,len(strip))):
            
            #added efficiency, if the y values are already too far apart, don't continue
            #if (strip[j][1]-strip[i][1])**2 >= min_distance: break

            dsquared = (strip[i][0]-strip[j][0])**2 + (strip[i][1]-strip[j][1])**2
            min_distance = min(min_distance, dsquared)
            
    
    return min_distance

def naive_min_distance(x,y):
    min_distance = math.inf
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            dsquared = (x[i]-x[j])**2 + (y[i]-y[j])**2
            min_distance = min(min_distance, dsquared)
    min_distance = math.sqrt(min_distance)
    return min_distance

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list()
    for i in range(len(x)):
        points.append((x[i], y[i]))
    sx = sorted(points, key=lambda x: x[0])
    sy = sorted(points, key=lambda x: (x[1], x[0]))
    answer = math.sqrt(minimum_distance(sx,sy))
    print("{0:.9f}".format(answer))
