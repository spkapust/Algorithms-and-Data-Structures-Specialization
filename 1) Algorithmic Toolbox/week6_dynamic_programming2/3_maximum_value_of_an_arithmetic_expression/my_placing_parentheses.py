import math

# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    size = len(dataset) // 2 + 1
    M = [[None for x in range(size)] for y in range(size)]
    m = [[None for x in range(size)] for y in range(size)]
    for i in range(size):
        M[i][i] = int(dataset[i*2])
        m[i][i] = int(dataset[i*2])
    

    for s in range(1, size):
        for i in range(size-s):
            j = i + s

            #minandmax function
            mn = math.inf
            mx = -math.inf
            for k in range(i,j):
                op = dataset[2*k+1]
                min1 = m[i][k]
                max1 = M[i][k]
                min2 = m[k+1][j]
                max2 = M[k+1][j]
                a = evalt(min1,min2,op)
                b = evalt(min1,max2,op)
                c = evalt(max1,min2,op)
                d = evalt(max1,max2,op)
                mn = min(mn,a,b,c,d)
                mx = max(mx,a,b,c,d)
            
            m[i][j] = mn
            M[i][j] = mx

    return M[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
