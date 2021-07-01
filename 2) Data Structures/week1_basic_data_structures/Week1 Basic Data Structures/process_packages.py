# python3

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
            
        finishes_before = 0
        for time in self.finish_time:
            if time <= request.arrived_at:
                finishes_before += 1
            else: break
        
        for i in range(finishes_before):
            self.finish_time.popleft()
        
        if len(self.finish_time) < self.size:
            last = 0 if len(self.finish_time) == 0 else self.finish_time[-1]
            start = max(last, request.arrived_at)
            end = start + request.time_to_process
            self.finish_time.append(end)
            return Response(False, start)
        else:
            return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
