# python3

import sys

num_reads = 1618
read_len = 100
err = .01

reads = []
for _ in range(num_reads):
    s = sys.stdin.readline().strip()
    reads.append(s)

def check_overlap(first, second, len, read_len):
    mismatches = 0
    s1 = first[read_len-len:]
    s2 = second[0:len]
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            mismatches += 1
            if mismatches > 2:
                return False
    return True


visited = [False] * num_reads
path = []

#genome = reads[0]
last_read = reads[0]
visited[0] = True
num_visited = 1
genome_length = read_len

while num_visited < num_reads:
    #find greatest overlap
    idx, match_length = 0, 0
    for i in range(num_reads):
        if visited[i] == False:
            for j in range(read_len):
                if (read_len - j) < match_length or (read_len - j) < 20:
                    break
                if check_overlap(last_read, reads[i], read_len-j, read_len):
                    idx, match_length = i, read_len - j
                    break
    
    visited[idx] = True
    last_read= reads[idx]
    num_visited+=1
    genome_length += read_len - match_length
    path.append((idx, match_length))


#get rid of overlap at the end
match_length = read_len
while match_length > 0:
    if check_overlap(last_read, reads[0], match_length, read_len):
        break
    match_length -= 1
genome_length -= match_length


counts = [[0 for _ in range(4)] for _ in range(genome_length)]
current_index = 0


for i, c in enumerate(reads[0]):
    if c=="A":
        counts[i][0] += 1
    elif c=="C":
        counts[i][1] += 1
    elif c == "G":
        counts[i][2] += 1
    else:
        counts[i][3] += 1

for idx, match_length in path:
    current_index += read_len - match_length
    for ix, c in enumerate(reads[idx]):
        i = (ix+current_index) 
        if i >= genome_length:
            i = i % genome_length
        if c=="A":
            counts[i][0] += 1
        elif c=="C":
            counts[i][1] += 1
        elif c == "G":
            counts[i][2] += 1
        else:
            counts[i][3] += 1

genome = ''
for i in range(genome_length):
    c = counts[i].index(max(counts[i]))
    if c==0:
        print('A', end='')
        #genome+='A'
    elif c==1:
        print('C', end='')
        #genome+='C'
    elif c == 2:
        print('G', end='')
        #genome+='G'
    else:
        print('T', end='')
        #genome+='T'

print(genome)









