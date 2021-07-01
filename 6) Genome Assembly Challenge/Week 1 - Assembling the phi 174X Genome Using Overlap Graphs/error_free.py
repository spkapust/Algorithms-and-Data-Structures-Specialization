# python3

import sys

num_reads = 1618
read_len = 100

reads = []
for _ in range(num_reads):
    s = sys.stdin.readline().strip()
    reads.append(s)

visited = [False] * num_reads

genome = reads[0]
last_read = reads[0]
visited[0] = True
num_visited = 1

while num_visited < num_reads:
    #find greatest overlap
    idx, match_length = 0, 0
    for i in range(num_reads):
        if visited[i] == False:
            for j in range(read_len):
                if (read_len - j) < match_length:
                    break
                if reads[i].startswith(last_read[j:]):
                    idx, match_length = i, read_len - j
                    break
    
    visited[idx] = True
    last_read= reads[idx]
    genome += last_read[match_length:]
    num_visited+=1

#get rid of overlap at the end
match_length=read_len
while match_length > 0:
    if reads[0].startswith(last_read[read_len - match_length:]):
        break
    match_length -= 1
genome = genome[:-match_length]


print(genome)


