# python3
from collections import namedtuple
AssignedJob = namedtuple("AssignedJob", ["worker","started_at"])

def SiftDown(i, data):
    last_index = len(data) - 1
    max_index = i 
    
    r = 2*i + 2
    if r <= last_index and data[r][1] <= data[max_index][1]:
        if data[r][1] == data[max_index][1]:
            if min(data[r][0], data[max_index][0]) == data[r][0]: max_index = r
        else: max_index = r

    
    l = 2*i + 1
    if l <= last_index and data[l][1] <= data[max_index][1]:
        if data[l][1] == data[max_index][1]:
            if min(data[l][0], data[max_index][0]) == data[l][0]: max_index = l
        else: max_index = l
            
    if max_index != i:
        data[i], data[max_index] = data[max_index], data[i]
        SiftDown(max_index, data)

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    min_heap = []
    for i in range(n_workers):
        min_heap.append([i, 0])
   
    result = []
    for job in jobs:
        result.append(AssignedJob(min_heap[0][0], min_heap[0][1]))
        min_heap[0][1] += job
        SiftDown(0, min_heap)
      
        

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
