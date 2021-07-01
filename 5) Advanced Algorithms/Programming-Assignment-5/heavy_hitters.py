# python3

import sys
import random
import math
from statistics import median

#D = dict()
bucket_sign_assignment = dict()

n = int(sys.stdin.readline().strip())
t = int(sys.stdin.readline().strip())

buckets = int(math.log(n) * 1500)
hash_functions = int(math.log(n) + 1)

p = 2**61-1

bucket_and_sign_params = []
for _ in range(hash_functions):
    a = random.randint(1,p-1)
    b = random.randint(1,p-1)
    c = random.randint(1,p-1)
    d = random.randint(1,p-1)
    bucket_and_sign_params.append((a,b,c,d))
    #bucket_and_sign_params.append((a,b))

def get_bucket_and_sign(id,i):
    a,b,c,d = bucket_and_sign_params[i]
    #a,b = bucket_and_sign_params[i]
    bucket = int(((a*id + b) % p) % buckets)
    #sign = 1 if bucket <= buckets else -1
    sign = int(((c*id + d) % p) % 2)
    if sign == 0: sign = -1
    return bucket, sign

counter = [[0 for _ in range(buckets)] for _ in range(hash_functions)]

for _ in range(n):
    id, value = [int(i) for i in sys.stdin.readline().strip().split()]
    #assert(id not in D)
    #D[id] = value
    for i in range(hash_functions):
        bucket, sign = get_bucket_and_sign(id, i)
        counter[i][bucket] += value*sign 
    

for _ in range(n):
    id, value = [int(i) for i in sys.stdin.readline().strip().split()]
    #assert(id in D)
    #D[id] -= value
    for i in range(hash_functions):
        bucket, sign = get_bucket_and_sign(id, i)
        counter[i][bucket] -= value*sign
    

num_queries = int(sys.stdin.readline().strip())
queries = list(map(int, sys.stdin.readline().strip().split()))
assert(len(queries) == num_queries)

for query in queries:
    # if D[query] >= t:
    #     print("1 ", end="")
    # else:
    #     print("0 ", end="")
    #print(query)
    counts = []
    for i in range(hash_functions):
        bucket, sign = get_bucket_and_sign(query, i)
        counts.append(counter[i][bucket] * sign)
    if median(counts) >= t:
        print("1 ", end="")
    else:
        print("0 ", end="")


