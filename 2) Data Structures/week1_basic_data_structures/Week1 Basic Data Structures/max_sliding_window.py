# python3
from collections import deque 


def max_sliding_window_naive(sequence, m):
    maximums = []
    dq = deque()
    dq.append(0)
    for i in range(1,m-1):
        while sequence[i] >= sequence[dq[-1]]:
            dq.pop()
            if len(dq) == 0 : break
        dq.append(i)


    for i in range(0, len(sequence) - m + 1):
        if dq[0] < i:
            dq.popleft()
        
        if len(dq) != 0:
            while sequence[i+m-1] >= sequence[dq[-1]]:
                dq.pop()
                if len(dq) == 0 : break
        dq.append(i+m-1)
        maximums.append(sequence[dq[0]])

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

