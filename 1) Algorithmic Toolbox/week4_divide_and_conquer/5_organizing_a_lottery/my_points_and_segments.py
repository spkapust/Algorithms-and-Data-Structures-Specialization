# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    counts = {}
    #write your code here
    line = []
    for start in starts:
        line.append((start, 'l'))
    for end in ends:
        line.append((end, 'r'))
    for point in points:
        line.append((point, 'p'))
    line.sort()
    lefts = 0
    for node in line:
        if node[1] == 'l': lefts += 1
        elif node[1] == 'r': lefts -= 1
        else: counts[node[0]] = lefts
    for i in range(len(points)):
        cnt[i] = counts[points[i]]
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
