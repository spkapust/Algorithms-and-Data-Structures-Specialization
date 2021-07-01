# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    l = left
    r = ave
    for i in range(left, right):
        if l == ave: 
            b[i] = a[r]
            r += 1
        elif r == right: 
            b[i] = a[l]
            l += 1
        elif a[l] <= a[r]:
            b[i] = a[l]
            l += 1
        else:
            b[i] = a[r]
            number_of_inversions += (ave-l)
            r += 1
    for i in range(left, right):
        a[i] = b[i]
    #print(a)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
