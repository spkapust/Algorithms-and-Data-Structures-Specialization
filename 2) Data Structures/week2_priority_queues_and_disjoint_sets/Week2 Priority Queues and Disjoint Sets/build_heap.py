# python3


def SiftDown(i, data, swaps):
    last_index = len(data) - 1
    max_index = i 
    
    r = 2*i + 2
    if r <= last_index and data[r] < data[max_index]:
        max_index = r

    l = 2*i + 1
    if l <= last_index and data[l] < data[max_index]:
        max_index = l
            
    if max_index != i:
        swaps.append((i,max_index))
        data[i], data[max_index] = data[max_index], data[i]
        SiftDown(max_index, data, swaps)

def build_heap(data):

    last_index = len(data) - 1 
    first = (last_index - 1) // 2 #first index to check
    swaps = []

    for i in reversed(range(first+1)):
        SiftDown(i,data,swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
