# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l
    count = 0
    #print(a[l:r+1])
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
            if a[j] == x: count+=1
            #print(a[l:r+1])
        if a[j] < x and count > 0:
            a[j-count], a[j] = a[j], a[j-count] 
            #print(a[l:r+1])
    a[l], a[j-count] = a[j-count], a[l]
    #print(a[l:r+1])
    return j-count, j

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort_two(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a,l,r)
    randomized_quick_sort_two(a, l, m - 1);
    randomized_quick_sort_two(a, m + 1, r);

def randomized_quick_sort_three(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort_three(a, l, m1 - 1);
    randomized_quick_sort_three(a, m2 + 1, r);

if __name__ == '__main__':
    for i in range(10**5):
        n = random.randint(1,100)
        a = [random.randint(1,1000) for x in range(n)]
        b = a.copy()
        c = a.copy()
        randomized_quick_sort_two(b, 0, n-1)
        randomized_quick_sort_three(c, 0, n-1)
        if b!=c:
            print("OG list: {}".format(a))
            print("right answer: {}".format(b))
            print("yours: {}".format(c))
            for index, (first, second) in enumerate(zip(b, c)):
                if first != second:
                    print(index, first, second)
            break
        
    print("DONE")


