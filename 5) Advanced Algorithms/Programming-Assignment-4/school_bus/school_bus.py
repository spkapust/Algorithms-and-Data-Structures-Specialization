# python3
import itertools 
INF = 10 ** 9

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def naive_optimal_path(graph):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    n = len(graph)
    best_ans = INF
    best_path = []

    for p in itertools.permutations(range(n)):
        cur_sum = 0
        for i in range(1, n):
            if graph[p[i - 1]][p[i]] == INF:
                break
            cur_sum += graph[p[i - 1]][p[i]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum < best_ans:
                best_ans = cur_sum
                best_path = list(p)

    if best_ans == INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])

def optimal_path(graph):
    #print(graph)
    n = len(graph)
    dp = {}

    #set initial state
    for i in range(1,n):
        subset_bit_mask = 1 << i
        dp[(i, subset_bit_mask)] = (graph[0][i], 0)
    

    for subset_size in range(2,n):
        for subset in itertools.combinations(range(1,n), subset_size):

            #set bits
            subset_bit_mask = 0
            for num in subset:
                subset_bit_mask |= 1 << num
            
            
            for num in subset:
                prev_bit_mask = subset_bit_mask & ~(1 << num)
            
                dists = []
                for j in subset:
                    if j == num: continue
                    a = dp[(j, prev_bit_mask)][0]
                    b = graph[j][num]
                    if a == INF or b == INF:
                        dists.append((INF,j))
                    else:    
                        dists.append((a+b,j))
                    dp[(num, subset_bit_mask)] = min(dists)
    
    dists = [] 
    prev_bit_mask = (2**n - 1) - 1
    for j in range(1,n):
        a = dp[(j, prev_bit_mask)][0]
        b = graph[j][0]
        if a == INF or b == INF:
            dists.append((INF,j))
        else:    
            dists.append((a+b,j))
        result = min(dists)
    
    best_ans = result[0]
    if best_ans == INF: 
        return (-1,[])
    else:
        best_path = []
        last = result[1]
        last_mask = prev_bit_mask
        while(last != 0):
            best_path.append(last)
            last, last_mask = dp[(last, last_mask)][1], last_mask ^ (1 << last)
        best_path.append(0)
        best_path.reverse()
        return (best_ans, [x + 1 for x in best_path])

if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
