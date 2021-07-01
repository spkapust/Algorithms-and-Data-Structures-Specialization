# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here

    mid = (left + right - 1) // 2
    leftmaj = get_majority_element(a, left, mid + 1)
    rightmaj = get_majority_element(a, mid + 1, right)

    if leftmaj == rightmaj: return leftmaj
    else:
        leftcount = 0
        rightcount = 0
        for i in range(left, right):
            if a[i] == leftmaj: leftcount += 1
            if a[i] == rightmaj: rightcount += 1
        if leftcount > rightcount and leftcount > (right - left)/2: return leftmaj
        if rightcount > leftcount and rightcount > (right - left)/2: return rightmaj

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
