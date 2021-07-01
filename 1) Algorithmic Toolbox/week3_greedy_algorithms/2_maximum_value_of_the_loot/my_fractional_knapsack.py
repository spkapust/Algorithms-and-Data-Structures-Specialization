# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    densities = []
    for i in range(len(weights)):
        densities.append(values[i] / weights[i])
    swd = []
    for i in range(len(weights)):
        swd.append((weights[i], densities[i]))
    
    swd.sort(key=lambda pair: pair[1], reverse=True)
    

    for i in range(len(swd)):
        if capacity == 0: break
        add = min(capacity, swd[i][0])
        capacity -= add
        value += add*swd[i][1]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
